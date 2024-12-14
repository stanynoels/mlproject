from setuptools import find_packages,setup
from typing import List


HYPHEN_E_DOT = '-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements
    '''
    requiremnts = []
    with open(file_path) as file:
        requiremnts = file.readlines()
        requiremnts = [req.replace("\n", "") for req in requiremnts]

        if HYPHEN_E_DOT in requiremnts:
            requiremnts.remove(HYPHEN_E_DOT)

    return requiremnts


setup(
name='mlproject',
version='0.0.1',
author='Noel Stany',
author_email='stanynoel4@gmail.com',
packages=find_packages(),
py_modules=get_requirements("requirements.txt"),
)