from setuptools import find_packages,setup
import os 
from typing import List

def get_requirements(file_name:str)->List[str]:
    requirements=[]
    with open(file_name) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        
        if "-e ." in requirements:
            requirements.remove("-e .")
    return requirements

setup(
    name='mlproject',
    version= '0.0.1',
    author='Siddhant Sharma',
    author_email="sidsharma2401@gmail.com",
    packages = find_packages(),
    install_requires=get_requirements('requirements.txt')
)