# setup.py
from setuptools import setup, find_packages

setup(
    name="fred-project",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'fredapi==0.5.2',
        'pandas>=2.1.0',
        'python-dotenv>=1.0.0',
        'requests>=2.31.0',
    ],
)