from setuptools import find_packages,setup
from typing import List 

def get_requirements(filepath:str)->List[str]:
    pass

setup(
    name = "Praveen",
    version="0.0.1",
    author="Praveen_p",
    author_email="praveen.dsmlai@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')


)