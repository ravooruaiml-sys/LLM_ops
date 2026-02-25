from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="LLM-OPS",
    version="0.1",
    author="ravooru",
    packages=find_packages(),
    install_requires = requirements,
)