# Award-Portal
Simple award application where users can see the projects posted,register and also submit their own projects,users can also vote on the project from variuos prospectives
# By Vinny Otach

# Application
<img src="/home/moringaschool/Documents/django projects/Awards/static/pics/Screenshot from 2018-12-21 15-47-19.png">

# User Stories
As a user of the application I should be able to:
<ul>
<li>View posted projects and their details.</li>
<li>Post a project.</li>
<li>Rate other users projects</li>
<li>Search for projects.</li>
<li>View my profile page</li>
</ul>

# Set up and Installations
<ol>
<li>git clone https://github.com/vinnyotach7/Awards-Portal.git</li>
<li>cd Awards</li>
<li>source virtual/bin/activate</li> 
<li>Install all the necessary requirements by running pip install -r requirements.txt (Python 3.6).
    $ ./manager.py runserver</li>
<li>
</ol>

# How to prepare environment variables
Since one needs a virtual enviroment, Create a virtual file and add the following configutions to it
<ul>
<li>SECRET_KEY= #secret key will be added by default</li>
<li>DEBUG= #set to false in production</li>
<li>DB_NAME= #database name</li>
<li>DB_USER= #database user</li>
<li>DB_PASSWORD=#database password</li>
<li>DB_HOST="127.0.0.1"</li>
<li> MODE= # dev or prod , set to prod during production</li>
<li>ALLOWED_HOSTS='.localhost', '.herokuapp.com', '.127.0.0.1'</li>
</ul>

# Cloning 
To clone this application on your terminal;https://github.com/vinnyotach7/Awards-Portal.git

# Creating Database
<ul>
<li>psql</li>
</ul>

# Migration
To make changes to the application and for you to see them take effect you should run the following commands;
<ol>
<li>python3.6 manage.py makemigrations</li>
<li>python3.6 manage.py migrate</li>
<li>Run python3.6 manage.py runserver</li>
</ol>

# Technologies Used
<ul>
<li>python3.6</li>
<li>Django</li>
<li>Bootstrap3</li>
<li>Postgres</li>
</ul>

# License
MIT Copyright (c) Vinny Otach


