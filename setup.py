from setuptools import setup

try:
    with open("README.md", "r", encoding="utf8") as f:
        README = f.read()
except FileNotFoundError:
    README = ""

setup(
    name="marilyn-api",
    version="0.1.1",
    description="Async client for Marilyn API",
    long_description=README,
    long_description_content_type="text/markdown",
    author="Pavel Maksimov",
    author_email="vur21@ya.ru",
    url="https://github.com/pavelmaksimov/marilyn-api",
    packages=["marilyn_api"],
    include_package_data=True,
    install_requires=["aiohttp>=3.8.1,<4.0.0"],
    python_requires=">=3.7,<4.0",
    extras_require={"pandas": ["pandas"]},
    license="MIT",
    zip_safe=False,
    keywords="client,api,python,marilyn",
    test_suite="tests",
)
