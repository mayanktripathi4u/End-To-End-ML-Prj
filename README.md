# End-To-End-ML-Prj

### Software and Tools Requirements

1. [Github Account](https://github.com)
2. [VS Code IDE](https://code.visualstudio.com)
3. [Heroku Account](https://heroku.com) or [AWS Account]()
4. [GitCLI](https://git-scm.com/book/en/v2/Getting-STarted-The-Command-Line) or [GitBash]()

## Create a new environment 
If using conda
```
conda create -p venv -y

conda activate venv/
```

If other 
```
pip install virtualenv
virtualenv venv
venv\Scripts\activate
```

## Install the Software using Requirement file
Make sure to create "requirements.txt" file.
```
pip install -r requirements.txt
```
## Push Code from Local to Git
```
git config --global user.name 

git config --global user.name "<Your Name>"

git config --global user.email

git config --global user.email "<Youe Email ID>"
```

## Commit the changes to Git.
```
git status

git add requirements.txt

git status

git add .

git commit -m "First Commit from Local to Git"

git push <remote> <branch>

git push origin main
```

## Create Application Using Flask
1. Create Flask app.
2. Using Postman to test the API.
    URL : http://127.0.0.1:5000/predict_api
    Raw Data in JSON Format
    ```
{
"data":{
"CRIM":0.00632,
"ZN": 18.0,
"INDUS":2.31,
"CHAS":0.0,
"NOX":0.538,
"RM":6.575,
"AGE":65.2,
"DIS":4.0900,
"RAD":1.0,
"TAX":296,
"PTRATIO":15.3,
"B":396.90,
"LSTAT":4.98
}
}    
```