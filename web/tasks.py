from celery import group, shared_task
import time


@shared_task
def add(x, y, wait=None):
    if wait:
        print(f'Processing task... adding up {x}, {y} with delay of {wait}')
        time.sleep(wait)
        print(f'Added up {x}, {y} with delay {wait} completed')
    return x + y


@shared_task
def group_add():
    print('Running a group of tasks')
    job = group([
            add.s(2, 2),
            add.s(4, 4, wait=5),
            add.s(8, 8, wait=7)
    ])
    print('job.apply_async running...')
    result = job.apply_async(retry=True, retry_policy={
                                                        'max_retries': 3,
                                                        'interval_start': 0,
                                                        'interval_step': 0.2,
                                                        'interval_max': 0.2,
                                                    })
    result.ready()  # have all subtasks completed?
    print('passed result.ready')
    result.successful()  # were all subtasks successful?
    print('passed result.successful')
