from setuptools import setup, find_packages

setup(
    name="cinematch",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "fastapi",
        "sqlalchemy",
        "pytest",
        "httpx",
        "python-jose[cryptography]",
        "passlib[bcrypt]",
        "python-multipart"
    ]
)