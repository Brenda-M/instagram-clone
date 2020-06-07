## Project Name

Instagram Clone

## Author Information

Muthoni Njuguna

## Description

This is an attempt rebuild the popular photo gallery website instagram with most of its functionalities using django. 

## Site 

View the website <a href="https://insta-dummy.herokuapp.com/login/?next=/">Here</a>

## User Stories
<ul>
  <li>Sign in to the application</li>
  <li>Upload Pictures to the application</li>
  <li>View a profile page with all pictures</li>
  <li>Follow other users and view the pictures on the timeline</li>
  <li>Like a picture and leave a comment on it. </li>
  <li>Search for other users</li>
</ul>

## Prerequisites
  
<ul>
  <li>Python</li>
  <li>Django</li>
  <li>Virtual environment</li>
</ul>

## Technologies and Tools Used

<ul>
  <li>Django</li>
  <li>Html</li>
  <li>Css</li>
  <li>Git Version Control</li>
</ul>


## Setup/Installation Requirements

Clone the repository below.

`git clone https://github.com/Brenda-M/instagram-clone.git`

Navigate to the root folder.

Create a virtual environment and activate it.

`python -m venv <name-of-environment>
source venv/bin/activate (Linux)
source venv/Scripts/activate (Windows)`

Install the requirements.

 `pip install -r requirements.txt.`

Create environmental variable file and add database configurations.

`touch .env`

Make a migrations.

`python manage.py makemigrations
python manage.py migrate`

Run the application.

`python manage.py runserver.`

## Contact Information

brendanjuguna1@gmail.com

## License

The MIT License (MIT) Copyright (c) 2020 Muthoni Njuguna.


