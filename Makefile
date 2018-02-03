setup:
	source ./setup.sh

run:
	python manage.py runserver

deploy:
	echo "Deleting old files"
	# Run rm on remote machine
	ssh root@138.68.185.197 "rm -rf /home/django/django_project"
	echo "Deploying website"
	# rsync is like scp but only copies different files from current dir to remote machine
	rsync -av --progress . root@138.68.185.197:/home/django/django_project --exclude ".git" --exclude "venv"

ssh:
	ssh root@138.68.185.197