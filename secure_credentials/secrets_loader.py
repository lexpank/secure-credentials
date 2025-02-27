from os import path
from yaml import safe_load
from secure_credentials.utils import decrypt_data


class CredentialsContainer(object):
    """A class to represent a container for credentials."""
    def __init__(self, credentials: dict):
        self._credentials = credentials

    def dig(self, *args):
        """Dig into the credentials."""
        value = None

        # Copy the credentials
        credentials = self._credentials.copy()

        for key in args:
            if key in credentials:
                value = credentials[key]
                credentials = value
            else:
                return None

        return value

    def get(self, key: str, default=None):
        return self._credentials.get(key, default)


def decrypt_credentials(env: str) -> CredentialsContainer:
    """ Decrypt credentials """

    # Check if the key exists
    if not path.exists(f"secrets/{env}.key"):
        print(f"Key for {env} does not exist!")
        return CredentialsContainer({})

    # Read encrypted data and key
    with open(f"secrets/{env}.key", "r") as f:
        key = f.read()

    if path.exists(f"secrets/{env}.yml.enc"):
        with open(f"secrets/{env}.yml.enc", "r") as f:
            data = f.read()
    else:
        print(f"Encrypted data for {env} does not exist!")
        return CredentialsContainer({})

    return CredentialsContainer(safe_load(decrypt_data(key, data)))
