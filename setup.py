from setuptools import find_packages, setup

setup(
    name="linkedin_api",
    version="2.0.0", 
    packages=find_packages(),
    install_requires=[
        "requests>=2.22.0",
        "urllib3>=1.25.3",
    ],
    python_requires=">=3.6",
)