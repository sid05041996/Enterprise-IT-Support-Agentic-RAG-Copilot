from pathlib import Path

#Current working directory
root=Path(".")  ##re-direct to the base directory..!!..,,;;

## -->> We can follow the ss named as "proper project structure explained"

#Folders to create
folders=[
    "app/api",
    "app/core",
    "app/rag",
    "app/services",
    "data",
    "templates",
    "static",
    "uploads",
    "tests",
]

## Files to be created.,;;:-:-:_:_.,;;
files=[
    "app/main.py",
    "requirements.txt",
    "ingest_sample_kb.py",
    "requirements.txt",
    "run.py",
    ".env",
]

## Process to create the / THE FOLDERS , now:-.,;;
for folder in folders:
    (root/folder).mkdir(parents=True, exist_ok=True)  ##if this folders exists then it will not create, otherwise will do.


## Process to create the / THE FILES , now:-.,;;
for file in files:
    (root/file).touch(exist_ok=True)  ## should be created within the root folder.  ~~>> since we are using the Path command hence we can use Linux commands like :- "touch".  

# def create_project()