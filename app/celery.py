from celery import Celery
from celery.schedules import crontab

app = Celery('app',
             include=['app.tasks.hello_world'])
app.config_from_object('app.celeryconfig')



app.conf.beat_schedule = {
    "everyday-task": {
        "task": "app.tasks.hello_world.group_add",
        "schedule": crontab(hour=15, minute=2)
    }
}