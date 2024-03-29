from setuptools import find_packages, setup

setup(
    name="PyApple",
    version="2.0.1",
    license="MIT",
    author="fxrcha",
    author_email="truetype24@gmail.com",
    description="Simple python library for dealing with Apple device's firmwares.",
    long_description=open("README.md", "r", encoding="UTF8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/fxrcha/PyApple",
    packages=find_packages(),
    install_requires=open("requirements.txt", "r", encoding="UTF8").read().splitlines(),
    classifiers=[
        "Programming Language :: Python :: 3.8",
    ],
    python_requires=">=3.8",
)
