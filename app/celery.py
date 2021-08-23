from celery import Celery
from celery.schedules import crontab

app = Celery('app',
             backend='redis://localhost:6379/0',
             broker='redis://localhost:6379/0',
             include=['app.tasks.hello_world', 'app.tasks.tasks'])
app.config_from_object('app.celeryconfig')

app.conf.beat_schedule = {
    "everyday-task": {
        "task": "app.tasks.hello_world.group_add",
        "schedule": crontab(hour=15, minute=2)
    }
}