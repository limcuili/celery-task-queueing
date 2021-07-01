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
5. See your wonderful creation in localhost:5000
6. When done, clean up whatever you may have left with `docker system prune`.