from setuptools import find_packages,setup

def get_requirements(file_path:str)

setup(
name='MLproject',
version='0.0.1',
author='Arghya',
author_email='deyarghyadeep5@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')


)