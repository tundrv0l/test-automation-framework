'''----------------- 
# Author: Parker Clark
# Date: 6/21/2024
# Description: A setup file for the library.
-----------------'''

from setuptools import setup, find_packages

# Setup information for the library
# TODO find the right versions for install_requires, add long_description and license
setup(
    name = 'raddish',
    url = 'https://github.com/pclark/test-automation-framework',
    packages = find_packages(include=['raddish']),
    version = '0.1.0',
    description = 'A custom library that extends the functionality of the pyautogui library.',
    author = 'Parker Clark',
    install_requires = ['pyautogui', 'tkinter'], 
    python_requires = '>=3.6',

)