init:
		docker-compose down && docker-compose run app sh -c "django-admin.py startproject app ." --remove-orphans

generate_module:
		docker-compose down && docker-compose run app sh -c "python manage.py startapp core" --remove-orphans

test:
		docker-compose down && docker-compose run app sh -c "python manage.py test && flake8" --remove-orphans

build:
		docker-compose down && docker-compose build

migrate:
		docker-compose down && docker-compose run app sh -c "python manage.py makemigrations core"

purge:
		docker-compose down && docker container prune && docker system prune