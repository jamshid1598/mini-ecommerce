### [mini eCommerce]()

![](https://www.creativefabrica.com/wp-content/uploads/2022/06/17/Ecommerce-Logo-Design-Graphics-32523051-1.jpg)


### SETUP PROJECT

`git clone https://github.com/jamshid1598/mini-ecommerce.git`


###### SETUP USUAL

- _create python virtual environment_  `python3 -m venv env`.
- _activate virtual environment_ `source env/bin/activate`.
- _upgrade python installer package pip_ `python3 -m pip install --upgrade pip`.
- _install all required dependencies from requirements.txt_ `python3 -m pip install -r requirements.txt`.
- _create_ `dev.py` _file in_ `prorot/settings/` _directory and copy contents from_ `dev.py.example` _in the docs folder then past into_ `.dev.py`.
- _create_ `.env` _file in project working directory, same folder level as_ `manage.py` _file in and copy contents from_ `.env.example` _in the docs folder then past into_ `.env`.
- _if you don't have a secret key use this command to generate new one_ `python3 -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'`
- _apply migrations_ `python3 manage.py makemigrations` _and_ `python3 manage.py migrate`.
- _create superuser_ `python3 manage.py createsuperuser`.
- _start server_ `python3 manage.py runserver`.


###### SETUP WITH DOCKER
- _create_ `dev.py` _file in_ `prorot/settings/` _directory and copy contents from_ `dev.py.example` _in the docs folder then past into_ `.dev.py`.
- _create_ `.env` _file in project working directory, same folder level as_ `manage.py` _file in and copy contents from_ `.env.example` _in the docs folder then past into_ `.env`.

1. _build image:_ 
    - `docker-compose -f docker-compose.dev.yml build`.
2. _run container_:
    - `docker-compose -f docker-compose.dev.yml up -d`.
3. _show logs on console (if you want):_
    - `docker-compose -f docker-compose.dev.yml logs -f`.
4. _navigate to_ [`http://localhost:8000/`](http://localhost:8000/) _to view the working django project_.
5. _stop containers:_
    - `docker-compose -f docker-compose.dev.yml down`.
6. _docker-compose config:_
    - `docker-compose -f docker-compose.dev.yml config`.

- _create migrations of model changes:_
    1. `docker-compose -f docker-compose.dev.yml run --rm backend python manage.py makemigrations`.
    - _or_
    2. `docker-compose -f docker-compose.dev.yml exec backend python manage.py makemigrations`.
- _apply migration to database:_
    1. `docker-compose -f docker-compose.dev.yml run --rm backend python manage.py migrate`.
    - _or_
    2. `docker-compose -f docker-compose.dev.yml exec backend python manage.py migrate`.
- _test project:_
    1. `docker-compose -f docker-compose.dev.yml run --rm backend python manage.py test`.
    - _or_
    2. `docker-compose -f docker-compose.dev.yml exec backend python manage.py test`.

## dumpdata and loaddata

- _import data to fixture file_ `docker-compose -f docker-compose.dev.yml run --rm backend python3 manage.py dumpdata <app>.<model> --indent 4 > apps/<app>/fixtures/<filename>.json`
- _export data from fixture file_ `docker-compose -f docker-compose.dev.yml run --rm backend python3 manage.py loaddata apps/<app>/fixtures/<filename>.json`


### USEFULL DOCKER COMANDS
- _remove all images, volumes and containers in docker_ `docker system prune`.
- _for removing all stoped and running containers, images and volumes_ `docker system prune -a`.
- _for removing all containers_ `docker rm -f $(docker ps -aq)`.
- _for removing all images_ `docker rmi $(docker images -q)` _removing by name_ `docker rmi <name>`.
