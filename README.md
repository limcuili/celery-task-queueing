# Using Celery for Orchestrating Tasks 
There are three main actions of using Celery, to be performed in this order:
1. Establish a message transport (broker) - for this project, we will use Redis.
2. Get workers ready to perform tasks given
3. Call the tasks

## Redis - our broker
Fun fact: Redis stands for '**Re**mote **Di**ctionary **S**erver', and it is an in-memory key-value data store.
Unfortunately for me, Redis Labs explicitly wrote 'Officially, Redis is not supported on Windows'.
So many users may consider the Windows-ported version of Redis by [MSOpenTech](https://github.com/microsoftarchive/redis).
So here we are... dockering it.

## Docker for Redis 
1. Download the repo
2. Start Docker
3. Run with `docker compose run`. Feel free to add a detach flag if you'd like, but make sure to do a `docker compose down` afterwards if you do.  
(Note that this is kicking off docker-compose.yml, and also building the Dockerfile container for the web directory.)
5. See your wonderful creation in localhost:5000
6. When done, clean up whatever you may have left with `docker system prune`.

At step 5 of the above, we have Redis running on our machine.

Now, finally, we can start on the fun stuff: Celery!

## Celery
Let's completely ignore our Flask app (app.py) for now, because that file was just a visual check that Redis works with docker.
Observe tasks.py - this is where we have our Celery task ready to go.
For a simple look, while you have Redis on, get on a new terminal to spin up a worker, and use the python console to execute a simple task:

```
$ celery -A web.celery worker --loglevel=INFO
$ cd web
$ python 

$ >> from tasks import add
$ >> add(4, 4, wait=3)
``` 
Just from the simple example above, we have given a Celery worker a task to do 4 + 4, with a 3 second delay. 

 