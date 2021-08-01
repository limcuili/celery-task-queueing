from app.celery import app
from celery import group, shared_task
import time


@shared_task
def add(x, y, wait=None):
    if wait:
        print(f'Processing task... adding up {x}, {y} with delay of {wait}')
        time.sleep(wait)
        print(f'Added up {x}, {y} with delay {wait} completed')
    else:
        print(f'Added up {x}, {y} completed')
    return x + y


@shared_task
def group_add():
    print('Running a group of tasks')
    task_list = []
    for i in range(3):
        task_list.append(add.s(i,i, wait=i))
        print(f'task_list: {task_list}')
    job = group(task_list)
    print('job.apply_async running...')
    result = job.apply_async(retry=True, retry_policy={
                                                        'max_retries': 3,
                                                        'interval_start': 0,
                                                        'interval_step': 0.2,
                                                        'interval_max': 0.2,
                                                    })
    # result.ready()  # have all subtasks completed?
    # print('passed result.ready')
    # result.successful()  # were all subtasks successful?
    # print('passed result.successful')
