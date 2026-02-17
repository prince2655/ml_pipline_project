from setuptools import setup,find_packages
from typing import List
HYPHON_E_DOT="-e ."

def get_requriments(filepath: str)->List[str]:
    requirenment=[]
    with open(filepath)as file_obj:
        requirenment=file_obj.readlines()
        requirenment=[i.replace("\n","") for i in requirenment]

        if HYPHON_E_DOT in requirenment:
            requirenment.remove(HYPHON_E_DOT)



setup(
   name='ml_pipline_project',
   version='0.0.1',
   description='machine learning pipline project',
   author='Prince karad',
   author_email='princekarad07@gmail.com',
   packages=find_packages(), 
   install_requires=get_requriments('requirenment.txt') 
)
