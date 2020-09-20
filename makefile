purge:
		docker-compose down && docker container prune && docker system prune

image:
		docker build .

init:
		make purge && docker-compose run app sh -c "django-admin.py startproject app ." --remove-orphans

generate_module:
		docker-compose down && docker-compose run app sh -c "python manage.py startapp core" --remove-orphans

test:
		docker-compose down && docker-compose run app sh -c "python manage.py test && flake8" --remove-orphans

build:
		docker-compose build

migrate:
		docker-compose down && docker-compose run app sh -c "python manage.py makemigrations core"

lint:
		pre-commit run -a

commit:
		pre-commit run -a && git add . && git commit -a

push:
		git push -u origin master 

run:
		docker-compose down && docker-compose up --build --remove-orphans
