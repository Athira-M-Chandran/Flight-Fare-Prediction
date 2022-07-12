# Flight-Fare-Prediction
The goal is to predict the fares of the flights based on different factors available in the provided dataset.

### Conda Environment

Creating conda enivronment
```
conda create -p venv python==3.7 -y
```
Activate conda environment
```
conda init.exe
conda activate venv/
```
### Requirements

write libraries to install in requirements.txt

create and run setup.py (Project name, version, author etc.)
```
python setup.py install
```

### GIT commands
To Add files to git
```
git add .
```
OR
```
git add <file_name>
```
 
> Note: To ignore file or folder from git we can write name of file/folder in .gitignore file

To check the git status
```
git status
```
To check all version maintained by git
```
git log
```
To create version/commit all changes by git
```
git commit -m "message"
```
To send version/changes to github
```
git push origin main
```
To check remote url
```
git remote -v
```

### To setup CI/CD pipeline in heroku we need 3 information

1. HEROKU_EMAIL = athiramchandran90@gmail.com
2. HEROKU_API_KEY = <>
3. HEROKU_APP_NAME = <>


### BUILD DOCKER IMAGE
```
docker build -t <image_name>:<tagname> .
```
> Note: Image name for docker must be lowercase

To list docker image
```
docker images
```
Run docker image
```
docker run -p 5000:5000 -e PORT=5000 f8c749e73678
```
To check running container in docker
```
docker ps
```
To stop docker conatiner
```
docker stop <container_id>
```

### Install ipkernel
```
pip install ipykernel
```

**Data Drift: When your datset stats gets change we call it as data drift**

Logger
Exeception
component


