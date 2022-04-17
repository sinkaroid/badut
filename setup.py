import re
from setuptools import setup

version = ""
with open("badut/__init__.py") as f:
    version = re.search(
        r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE
    ).group(1)


if not version:
    raise RuntimeError("version is not set")

readme = ""
with open("README.md", encoding="utf8") as f:
    readme = f.read()

setup(
    name="badut",
    author="sinkaroid",
    author_email="anakmancasan@gmail.com",
    version=version,
    long_description=readme,
    url="https://github.com/sinkaroid/badut",
    project_urls={
        "Funding": "https://paypal.me/sinkaroid",
        "Issue tracker": "https://github.com/sinkaroid/badut/issues/new/choose",
        "Documentation": "https://sinkaroid.github.io/badut",
    },
    packages=["badut"],
    license="MIT",
    classifiers=[
        "Framework :: AsyncIO",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Build Tools",
    ],
    description="Python HTTP client designed to be simple and async context",
    include_package_data=True,
    keywords=[
        "http",
        "https",
        "protocol",
        "fetch",
        "requests"
    ]
)
