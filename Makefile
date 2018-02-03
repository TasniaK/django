setup:
	source ./setup.sh

run:
	python manage.py runserver

deploy:
	echo "Deleting old files"
	ssh root@138.68.185.197 "rm -rf /home/django/django_project"
	echo "Deploying website"
	rsync -av --progress . root@138.68.185.197:/home/django/django_project --exclude ".git" --exclude "venv"

ssh:
	ssh root@138.68.185.197