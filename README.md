# Django Project with DRF & Template Rendering
This project integrates Django

This project integrates Django REST Framework (DRF) and traditional template rendering. You can access the login page via a browser, or interact with the API using Postman.


## postman documention : https://documenter.getpostman.com/view/44984967/2sB3HqJK7j

## Dockerhub link: 

## Github link: https://github.com/c-abhijith/Employee-Task-Management-System.git

## SETUP INSTRUCTIONS:
    Clone gitrepo:
                git clone https://github.com/c-abhijith/Employee-Task-Management-System.git
                
                cd Employee-Task-Management-System

    For Linux or macOS users:
                Run the following commands in your terminal:
                                make env-setup
                                make run-local

    For Windows users:

        Run the following commands in Command Prompt or PowerShell:

                                python3 -m venv venv
                                .\venv\Scripts\activate
                                pip install -r requirements.txt


                                python manage.py makemigrations
                                                or 
                                python manage.py makemigrations taskmanager


                                python manage.py migrate
                                                or 
                                python manage.py migrate taskmanager



                                python manage.py runserver

## Templated URL
        LoginUrl: http://127.0.0.1:8000/login/

## RestURL

        please follow postman url
        https://documenter.getpostman.com/view/44984967/2sB3HqJK7j





## You can create a superuser using the following command:         

            python manage.py createsuperuser
    
        Alternatively, a superuser has already been created with the following credentials:


                username : Superuser
                password : Password

## Admin and User password

                password : password

        

## TestCase

## Docker commands 
        -  docker-compose up --build
