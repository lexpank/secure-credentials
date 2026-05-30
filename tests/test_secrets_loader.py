import unittest

from secure_credentials_kit.secrets_loader import CredentialsContainer, normalize_credentials


class CredentialsContainerTests(unittest.TestCase):
    def test_empty_credentials_are_normalized_to_dict(self):
        container = CredentialsContainer(None)

        self.assertIsNone(container.get("SOME_ENV_VAR"))

    def test_mapping_credentials_support_get_and_dig(self):
        container = CredentialsContainer({"database": {"url": "postgres://example"}})

        self.assertEqual(container.get("database"), {"url": "postgres://example"})
        self.assertEqual(container.dig("database", "url"), "postgres://example")

    def test_string_credentials_raise_clear_error(self):
        with self.assertRaisesRegex(ValueError, "mapping at the root"):
            CredentialsContainer("SOME_ENV_VAR=secret")

    def test_list_credentials_raise_clear_error(self):
        with self.assertRaisesRegex(ValueError, "mapping at the root"):
            normalize_credentials(["secret"])

    def test_get_as_type_casts_existing_value(self):
        container = CredentialsContainer({"port": "5432"})

        self.assertEqual(container.get_as_type("port", int), 5432)

    def test_get_as_type_returns_default_cast_to_type(self):
        container = CredentialsContainer({})

        self.assertEqual(container.get_as_type("port", int, "5432"), 5432)

    def test_get_as_type_returns_none_for_missing_value_without_default(self):
        container = CredentialsContainer({})

        self.assertIsNone(container.get_as_type("port", int))

    def test_get_as_type_returns_cast_errors(self):
        container = CredentialsContainer({"port": "invalid"})

        with self.assertRaises(ValueError):
            container.get_as_type("port", int)

    def test_dig_as_type_casts_existing_value(self):
        container = CredentialsContainer({"database": {"port": "5432"}})

        self.assertEqual(container.dig_as_type(int, "database", "port"), 5432)

    def test_dig_as_type_returns_default_cast_to_type(self):
        container = CredentialsContainer({})

        self.assertEqual(container.dig_as_type(int, "database", "port", default="5432"), 5432)

    def test_dig_as_type_returns_none_for_missing_value_without_default(self):
        container = CredentialsContainer({})

        self.assertIsNone(container.dig_as_type(int, "database", "port"))

    def test_dig_as_type_returns_cast_errors(self):
        container = CredentialsContainer({"database": {"port": "invalid"}})

        with self.assertRaises(ValueError):
            container.dig_as_type(int, "database", "port")


if __name__ == "__main__":
    unittest.main()
