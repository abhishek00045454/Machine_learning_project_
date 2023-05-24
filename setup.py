from setuptools import find_packages,setup
from typing import List
Hypen_E_DOT="-e ."
def get_requirements(file_path:str)-> List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        
        if Hypen_E_DOT in requirements:
            requirements.remove(Hypen_E_DOT)
    
    return requirements  

setup(
    name="ML_project_setup",
    author="Anhishek Saini",
    version="0.0.01",
    author_email="abhisheksaini388@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)
