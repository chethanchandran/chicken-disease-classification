#This is where we define all the required folders of the project, run this file to create the same.
import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s:')

project_name='chicken_disease_classification'

list_of_files=[
    ".github/workflows/.gitkeep", #.gitkeep is a dummy file added just to keep the folder in git, git does not include folder if it is empty
    f"src/{project_name}/__init__.py", #Constructor file to make it available for imports
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",   
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",#Notebook for any trials done
    "templates/index.html"
]

#Any new file in the later stage, just add it here and run the template.py file only that file will be created.

for filepath in list_of_files:
    filepath=Path(filepath) #windows uses backward path but we have given forward path like linux, use Path will automatically convert in to windows backward slash.
    filedir, filename=os.path.split(filepath)

    if filedir!="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating Directory; {filedir} for the file :{filename}")

    if(not os.path.exists(filepath) or (os.path.getsize(filepath)==0)):
        with open(filepath,"w") as f:
            pass
            logging.info(f"Creating empty file:{filepath}")

    else:
        logging.info(f"{filename} already exists")