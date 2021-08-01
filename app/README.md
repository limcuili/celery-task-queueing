### Installing Redis
first time installation of redis `brew install redis`.

### Starting up a Redis Server
start redis server using configuration file `redis-server /usr/local/etc/redis.conf`.  
in a new terminal, test that the server is running `redis-cli ping`.  
kill the server `redis-cli shutdown`.

### Kick off a Celery beat and execute tasks
start the beat, then send workers to execute the tasks:  
`celery -A app beat --loglevel=INFO`  
`celery -A app worker --purge --loglevel=DEBUG`