from setuptools import setup, find_packages

setup(
    name="HangMan",
    version="1.0",
    author="jsyph",
    description="A HangMan game package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/jsyph/HangMan",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        "hangman": ["dictionary.json"],
    },
    install_requires=[],
    entry_points={
        "console_scripts": [
            "hangman=hangman:main",
        ],
    },
    python_requires=">=3.6",
)
