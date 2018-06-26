# User Profile

## Python web development project



For this project, you’ll build a form that takes in details about a registered user and displays those details on a profile page. The profile page should only be visible once the user has logged in.The profile page should include first name, last name, email, date of birth, confirm email, short bio and the option to upload an avatar


## Prerequisites


**Python** 3.5+ Installation
**Django** 2.0 Installation

## Resources
Simpleisbetterthancomplex.com tutorials were utilized for helping create user profile modules


## Steps:


1. First, set up a virtualenv. There are plenty
of tutorials online, so we won't cover it here.


2. Next, clone to repo to get the code


   git clone https://github.com/BrandonOakes/user_profile_with_django.git


3. From within the newly-cloned directory, install program requirements


    	pip install - requirements.txt


4. Next, migrate the database


    	python manage.py makemigrations


    	python manage.py migrate


5. Run server


    	python manage.py runserver
