# Development Database

If you are running the Django development server or the unit tests then you will need to run a database.

## prerequisites for running this database

1. Install Docker
2. Install Docker-compose

## How about I just install it on my operating system?

You can do that if you really want to BUT then you are on your own when you break it.

Docker is nice because absolutely everything you need to run a properly configured database is in this directory. And if you break it or want a clean system then resetting the db is trivial.

## Commands

To run the db:

```
docker compose up
```

To reset your development databases so that they are fresh and clean:

```
./cleanup_devdb.sh
docker-compose up
```

## Interacting with the databases via django

Once your composition is up and running:

```
python manage.py [any command that interacts with the database]
```

This just works.
