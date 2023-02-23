Project:
Making a simple polling web-application, where we can add question with choices from admin side.
Other users can open the given url to read the the question and vote for there desired choice.

Setup the project on local system:
1) Install python-3
    i) sudo apt-get update
   ii) sudo apt-get install python3
  iii) sudo apt install python3-pip
2) Create a virtual environment and activate it.
    i) pip install virtualenv
   ii) virtualenv venv
  iii) venv\Scripts\activate (this is used to activate the virtual environment)
3) Install django.
    i) pip install django
4) Start the django project.
    i) django-admin startproject
5) Create the required apps.
    i) django-admin startapp (appname)
6) Register the apps in setting.py file.
7) Apply migrations and run the project.
    i) python manage.py makemigrations
   ii) python manage.py migrate
  iii) python manage.py runserver

Create a Docker image:
1) Write a dockerfile for the above setup.
2) Create and push the image on dockerhub

Deployment:
1) Create required infrastructure using IAC code.
2) Deploy the application on the EKS cluster.