import subprocess
import sys, platform
from os import path
from .get_sysinfo import (
    Username, PythonVersion, 
    _StrPythonVersion, winversion
)

def python_path():
    if sys.platform == "win32":
        _1 = f"C:/Users/{Username}/AppData/Local/Packages/PythonSoftwareFoundation"
        _2 = f"{_1}.Python.{PythonVersion}_qbz5n2kfra8p0/LocalCache/local-packages"
        _3 = f"{_2}/Python{_StrPythonVersion}/site-packages"
        return _3

class python:
    def install(package: str, argument=""):
        """
        :param argument: package==version, package>=version, etc...
        """
        if path.exists(f"{python_path}/{package}"):
            return f"Package {package} already exists"
        else:
            subprocess.Popen(f'python{PythonVersion} -m pip install {package}{argument}', shell=True)
    
    def execute(file: str):
        if not path.exists(file):
            raise FileNotFoundError(f'File {file} not found! try with another file')
        else:
            subprocess.Popen(f'python{PythonVersion} -m {file}', shell=True)
    
    def uninstall(package: str):
        if not path.exists(f"{python_path}/{package}"):
            raise FileNotFoundError(f'Package {package} not found! try installing it')
        else:
            subprocess.Popen(f'python{PythonVersion} -m pip uninstall {package}', shell=True)
    
    def upgrade(package: str):
        if not path.exists(f"{python_path}/{package}"):
            raise FileNotFoundError(f'Package {package} not found! try installing it')
        else:
            subprocess.Popen(f"python{PythonVersion} -m pip install --upgrade {package}", shell=True)
            