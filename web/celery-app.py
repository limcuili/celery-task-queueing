from celery import Celery
from .tasks import group_add

REDIS_URL = 'redis://redis:6379/0'
celery = Celery('tasks', broker=f'{REDIS_URL}', backend=f'{REDIS_URL}')
celery.autodiscover_tasks(['tasks'])


### beat
from celery.schedules import crontab

imports = ('tasks')
timezone = 'UTC'
celery.conf.beat_schedule = {
    'every-minute': {
        'task': 'tasks.group_add',
        'schedule': crontab(minute="*") # Every minute
    }
}
