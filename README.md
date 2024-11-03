### local development
```commandline
pipenv shell
pipenv install

# install docker
# then build docker container for db
docker run --rm --name psql1 \
-e POSTGRES_USER=postgres \
-e POSTGRES_PASSWORD=secret123 \
-p 5416:5432 \
-d postgres

# create DB da_tkpm
docker exec -it psql1 psql -U postgres -c 'CREATE DATABASE da_tkpm;

# run migrations
flask db upgrade

# run app => app will run on localhost:5000
flask run --debug

```

