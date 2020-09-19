init:
		docker-compose down && docker-compose run app sh -c "django-admin.py startproject app ." --remove-orphans

purge:
		docker-compose down && docker container prune && docker system prune