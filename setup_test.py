from setuptools import find_packages,setup   # find_packages within root folder (here its sensor folder). Setup will help on publishing and setting up the package
from typing import List

def get_requirements()->List[str]:  # get requirements function return list of strings
    """
    This function will return a list of requirements
    """
    requirements_list:List[str] = []    # defining a variable of type List[str]
    return requirements_list

setup(
    name="sensor",
    version="0.0.1",
    author="Bonny Philip",
    author_email="philipbonny18@gmail.com",
    packages= find_packages(),  # this will search for packages
    install_requires=get_requirements()
)


# Run the command "python setup.py install"
