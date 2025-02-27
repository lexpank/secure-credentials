from os import path, getenv, remove
from subprocess import run as subprocess_run
from yaml import safe_load, safe_dump
from django.core.management.base import BaseCommand
from secure_credentials.utils import encrypt_data, decrypt_data


class Command(BaseCommand):
    help = "Encrypt or decrypt data"

    def add_arguments(self, parser):
        parser.add_argument("env", type=str, help="Environment name")

    def handle(self, *args, **kwargs):
        env = kwargs["env"]
        key = None
        editor = getenv("EDITOR", "nano")

        # Check if the key exists
        if not path.exists(f"secrets/{env}.key"):
            print(f"Key for {env} does not exist!")
            return

        with open(f"secrets/{env}.key", "r") as f:
            key = f.read()

        if path.exists(f"secrets/{env}.yml.enc"):
            with open(f"secrets/{env}.yml.enc", "r") as f:
                encrypted_data = f.read()
        else:
            encrypted_data = encrypt_data(key, "")

        decrypted_data = decrypt_data(key, encrypted_data)

        with open(f"secrets/{env}.yml", "w") as f:
            f.write(decrypted_data)

        subprocess_run([editor, f"secrets/{env}.yml"])

        with open(f"secrets/{env}.yml", "r") as f:
            yaml_data = safe_load(f)

        encrypted_data = encrypt_data(key, safe_dump(yaml_data))

        with open(f"secrets/{env}.yml.enc", "w") as f:
            f.write(encrypted_data)

        # Remove the unencrypted file
        remove(f"secrets/{env}.yml")

        print(f"Data has been encrypted and saved to secrets/{env}.yml.enc")

