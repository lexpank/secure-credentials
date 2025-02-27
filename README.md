# Django Secure Credentials 🔐

A secure, encrypted credentials system for Django, inspired by Rails credentials.

## Features
- Environment-specific encrypted credentials
- Simple management commands (edit, show, generate key)  

## Installation
```sh
pip install django-secure-credentials
```

## Usage

Add `secure_credentials` to your `INSTALLED_APPS` in `settings.py`:

```python
INSTALLED_APPS = [
    ...
    'secure_credentials',
    ...
]
```

Add secret keys to `.gitignore`:

```sh
echo "secrets/*.key" >> .gitignore
````

Run the following command to generate a new key and credentials file:

```sh
python manage.py credentials_generate_key <environment>
```

This will create a new key and credentials file at `config/credentials.yml.enc`.

To edit the credentials file, run:

```sh
python manage.py credentials_edit <environment>
```