# django project

run 'source setup.sh' to set up python venv and install dependencies from requirements.txt

to setup with Makefile (If this fails use command above):

`make setup`

to connect to box using secure shell command 'ssh root@138.68.185.197':

`make ssh`

to run the server locally: 'python manage.py runserver' or:

`make run`

to get all (i.e -r) project files, used 'scp -r root@138.68.185.197:/home/django/django_project .' copies django-project to current directory (i.e. .)

to deploy / copy all files to remote machine run:

`make deploy`




