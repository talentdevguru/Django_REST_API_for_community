# Django_REST_API_for_community

This is Django Project to provide the rest API for Community Feature.

Current Project use the Python/Django with several Django Pakages.

Install Guide.
1. Environmental settings

Check the Python version. If you do not have Python version 3.x, install it.
$ python --version
$ python3 --version

Then install virtualenv to set up the virtual environment.
$ apt-get install virtualenv

Once the virtualenv installation is complete, create a virtual environment for learning.
$ virtualenv -p python3 rest_env

When the virtual environment is created, the virtual environment is activated. If (rest_env)it worked, it will be placed in front of the terminal input window .
$ source ~/rest_env/bin/activate

Then install the necessary Django and Python libraries.
$ pip install django
$ pip install djangorestframework
$ pip install -U drf-yasg
$ pip install flex

Now you have to move to project directory.

Migrate the database.
$python manage.py makemigrations
$python manage.py migrate

Then Run server.
$python manage.py runserver

And you can check the api list on 
http://localhost:8000/api/v1
http://localhost:8000/swagger/v1
http://localhost:8000/redoc/v1


Question, User, Answer Model(database) are related each other.
So we can get related data from api.

Also you can manage them the admin page.
For that, you have to create the superuser.
$python manage.py createsuperuser
then will be required username, email, password.

And then you can run server again.
Then visit admin panel.
http://localhost:8000/admin


