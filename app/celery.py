from celery import Celery
from celery.schedules import crontab

app = Celery('app',
             include=['app.tasks'])
app.config_from_object('app.celeryconfig')



app.conf.beat_schedule = {
    "everyday-task": {
        "task": "app.tasks.group_add",
        "schedule": crontab(minute="*")
    }
}