from setuptools import find_packages,setup   # find_packages within root folder (here its sensor folder). Setup will help on publishing and setting up the package
from typing import List

setup(
    name="sensor",
    version="0.0.1",
    author="Bonny Philip",
    author_email="philipbonny18@gmail.com",
    packages= find_packages(),  # this will search for packages
    install_requires=[]
)

# Run the command "python setup.py install"