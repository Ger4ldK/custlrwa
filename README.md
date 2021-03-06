# Git Bash
1. Make sure you are in your directory

```
<!-- git bash ui --!>
/custlrwa (your name)
$
```

2. Committing and Pushing

```
git add .
git commit -m "insert description of changes made"
git push
```
3. Check branch is up to date

```
git status
```
4. To update the latest code from staging
```
git checkout staging
git pull
git checkout *your branch name*
git merge staging
```

# custlrwa
Custlr Web Application


# Description of project
The basic idea is to create something similar to Booking.com, where a web/mobile app will search other websites for tailored clothes specific to the user's specification. Users should ble able to find a listing of companies/shops which cater to their specific request. 

# Frontend
**Hariz, Hanis, Nooh**

We will start our frontend development using **src boighor** by using their default vanilla javascript and html5. We will customise the template as minimalistic as possible

*To-Do*

# Backend
**Gerald, Brandon, Raadi**

The plan for this is a REST API done in Django REST Framework(DRF), as Python is the best option for web scraping right now - DRF is also done in Python, so this makes implementation easier. 

The server is going to be hosted on a uni-provided URL, and HTTP requests will be made by the frontend to get a JSON file for information.

## Getting Started With Backend

*Make sure you have these installed:*
- python (3.7+, currently 3.7.6 64-bit)
- pip
- pipenv
- XAMPP


Run "pipenv install", and all dependencies for the project itself will be added in 

**EXCEPTION** - mysqlclient has issues when installed using 'pip install' so you'll have to install it using the following command - 'pipenv install mysqlclient-1.4.6-cp37-cp37m-win_amd64.whl'.

To check what packages are installed right now, run "pipenv run pip freeze"

*Currently, the project should have these installed when you run the above command:-*
- astroid==2.3.3
- beautifulsoup4==4.8.2
- colorama==0.4.3
- Django==2.2.9
- djangorestframework==3.11.0
- isort==4.3.21
- lazy-object-proxy==1.4.3
- mccabe==0.6.1
- mysqlclient==1.4.6
- pylint==2.4.4
- pytz==2019.3
- six==1.14.0
- soupsieve==1.9.5
- sqlparse==0.3.0
- typed-ast==1.4.1
- wrapt==1.11.2

### Once all the packages are installed, and there aren't any errors, run "pipenv shell" to enter the shell for the environment with all the packages installed

Inside the shell is where all the important packages will be installed. The reason why we use a virtual environment to keep all our packages, is so that we know exactly what packages we'll need in our project, and not anything from other projects, etc. To add a new package, install with "pipenv install packagename" i.e to install django I ran "pipenv install django". More information on pipenv can be found here: https://pipenv-fork.readthedocs.io/en/latest/basics.html

## Django

**XAMPP should be running before Django! Start Apache and MySQL first!**

To run the server and take a look at the changes made, run 'py manage.py runserver'. Migrations made for db - i.e new tables, changes to columns in tables, etc. will require you to run 'py manage.py migrate'.