# Using Celery for Orchestrating Tasks

## How to read this repo
I have a Windows. I also have a Mac. So you're essentially going to get two (not great) repos in one.   
Mac directory: ./app  
Windows directory: everything else (because we need docker, it takes the main directory as well as the ./web)

## A quick introduction of what I'm trying to do
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
3. From the project directory, run with `docker compose run`. Feel free to add a detach flag if you'd like, but make sure to do a `docker compose down` afterwards if you do.  
(Note that this is kicking off docker-compose.yml, and also building the Dockerfile container for the web directory.)
5. See your wonderful creation in localhost:5000
6. When done, clean up whatever you may have left with `docker system prune`.

At step 5 of the above, we have Redis running on our machine.

Now, finally, we can start on the fun stuff...

## Celery
Let's completely ignore our Flask app (app.py) for now, because that file was just a visual check that Redis works with docker.
In docker-compose.yml, you should see that it spins up the celery beat and celery worker through the celery-app.py file.
Unfortunately for me, I have not figured out why I am getting an error of `Received unregistered type of task 'tasks.group_add'`.
But here's a commit anyway, since I'm getting closer.   
