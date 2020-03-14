from setuptools import setup, find_packages

setup(
    name="docker-compost",
    version="0.1",
    packages=["compost"],
    install_requires=["pyyaml", "networkx", "matplotlib"],
    setup_requires=["wheel"],
    scripts=["compost/compost"],
)
