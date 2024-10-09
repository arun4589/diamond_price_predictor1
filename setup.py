from setuptools import find_packages, setup
from typing import List
HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str)->list[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        if HYPEN_E_DOT  in requirements:
            requirements.remove(HYPEN_E_DOT) 
        return requirements
setup(
    name='potato_disease_predictor',
    version='0.0.7',
    author='Arun',
    author_email='erarunkumawat50@gmail.com',
    install_requires=get_requirements('requirement.txt'),
    packages=find_packages()
)