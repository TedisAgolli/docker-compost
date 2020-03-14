from setuptools import setup, find_packages

setup(
    name="compost",
    version="0.1",
    packages=["compost"],
    install_requires=["pyyaml", "networkx", "matplotlib"],
    scripts=["compost/compost"],
)
