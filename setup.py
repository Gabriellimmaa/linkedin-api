from setuptools import find_packages, setup

setup(
    name="linkedin_api",
    version="2.0.1", 
    packages=find_packages(),
    install_requires=[
        "requests>=2.22.0",
        "urllib3>=1.25.3",
        "bs4>=0.0.2"
    ],
    python_requires=">=3.6",
)