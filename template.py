import os 
from pathlib import Path 
import logging

# logging.basicConfig(level=logging.INFO , format =

project_name = "mlproject"

list_of_files = [
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configurations.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html",

]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir  , filename = os.path.split(filepath)


    if filedir != "":
        os.makedirs(filedir , exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the filename : {filename}")

    if(not os.path.exists(filename)) or (os.path.getsize(filepath)==0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating Empty filesc :{filepath}")

    else :
        logging.info(f"File {filepath} already exists")