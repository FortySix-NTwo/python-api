#######################################################################################################
#													 GNU Makefile for project and Docker automation							  					 	  #
#																			Author: Jonathan Farber 																				#
#																								---																										#
#												  for more information please visit the linke bellow													#
#												  https://www.gnu.org/software/make/manual/make.html													#
#######################################################################################################
.PHONY: purge image init gen-core test build migrate lint commit push run Superuser

# Docker Container Shut-Down and Delete
purge:
		docker-compose down && docker container prune && docker system prune

# Build Docker Image
image:
		docker build .

# Init Docker-Compose Project
init:
		make purge && docker-compose run app sh -c "django-admin.py startproject app ." --remove-orphans

# Generate Django Core Module
gen-core:
		docker-compose down && docker-compose run app sh -c "python manage.py startapp core" --remove-orphans

# Generate Django Model
# @Params: NAME=name
gen-model:
		docker-compose run --rm app sh -c "python manage.py startapp ${NAME}"

# Unit Tests
test:
		docker-compose down && docker-compose run --rm app sh -c "python manage.py test && flake8" --remove-orphans

# Build Docker-Compose Container 
build:
		docker-compose build

# Migrate Database Changes 
migrate:
		docker-compose down && docker-compose run app sh -c "python manage.py makemigrations core"

# Check Syntax and Lint
lint:
		pre-commit run -a

# Git Commit with Pre-Commit lInting Checks
commit:
		pre-commit run -a && git add . && git commit -a

# GitHub Push Commit To Master
push:
		git push -u origin master 

# Run Docker-Compose Container 
run:
		docker-compose down && docker-compose up --build --remove-orphans

# Create Admin User with Superuser privlages 
superuser:
		docker-compose run app sh -c "python manage.py createsuperuser"
