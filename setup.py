# install local package in the virtual environment

from setuptools import setup, find_packages

setup(
    name='mcqgenerator',
    version='0.0.1',
    author='Shreya P',
    author_email='shreyap1908@gmail.com',
    install_requires=["openai", "langchain", "streamlit", "python-dotenv", "PyPDF2"],
    packages=find_packages()
)