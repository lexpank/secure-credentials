from os import path, mkdir
from django.core.management.base import BaseCommand
from secure_credentials.utils import generate_encryption_key

class Command(BaseCommand):
    help = "Generate a new encryption key"

    def add_arguments(self, parser):
        parser.add_argument("env", type=str, help="Environment name")

    def handle(self, *args, **kwargs):
        env = kwargs["env"]
        key = generate_encryption_key()

        # Check if the directory exists
        if path.exists(f"secrets/{env}.key"):
            print(f"Key for {env} already exists!")
            return

        # Create the directory if it doesn't exist
        if not path.exists("secrets"):
            mkdir("secrets")

        with open(f"secrets/{env}.key", "w") as f:
            f.write(key)

        print(f"Key for {env} has been generated and saved to secrets/{env}.key")
