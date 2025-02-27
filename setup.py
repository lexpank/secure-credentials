from setuptools import setup, find_packages

setup(
    name="django-secure-credentials",  # Package name
    version="0.1.0",  # Initial version
    description="A secure encrypted credentials system for Django, inspired by Rails credentials",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/lexpank/django-secure-credentials",  # Your GitHub repo
    packages=find_packages(exclude=["tests", "examples"]),  # Include all packages except tests
    install_requires=[
        "Django>=3.2",  # Requires Django 3.2 or later
        "cryptography>=41.0.0",  # Used for encryption
        "pyyaml>=6.0",  # YAML support for secrets storage
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Framework :: Django",
        "Topic :: Security",
    ],
    keywords=["django", "credentials", "encryption", "security"],
    python_requires=">=3.8",  # Require Python 3.8 or later
    project_urls={
        "Homepage": "https://github.com/lexpank/django-secure-credentials",
        "Issues": "https://github.com/lexpank/django-secure-credentials/issues",
    },
)
