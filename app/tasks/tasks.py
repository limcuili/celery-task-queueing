from app.celery import app
from celery import group, chain, shared_task
import time
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(module)s - %(message)s')
loglevels = {
    "CRITICAL": logging.CRITICAL,
    "WARNING": logging.WARNING,
    "INFO": logging.INFO,
    "DEBUG": logging.DEBUG,
    "": logging.INFO
}
logger.setLevel(logging.DEBUG)


@shared_task(bind=True, max_retries=3, default_retry_delay=0)
def multiply(self, num, string):
    multiply_complete = False
    if self.request.retries == self.max_retries:
        logging.debug(f'{string} hit max retries! returning.')
        return
    logging.debug(f'{string} multiply : BEGIN')
    try:
        if string == 'cuili':
            raise Exception('raising forced cuili exception')
        result = num*2
        for i in range(result):
            time.sleep(1)
            if i % 5 == 0:
                logging.debug(f'multiply {string} : {i}')
        multiply_complete = True
    except:
        multiply.retry()
    return multiply_complete


def waiting(num, string):
    logging.info(f'waiting for {string}...')
    for i in range(num):
        time.sleep(1)
        if i % 5 == 0:
            logging.debug(f'waiting for {string}: {i}')
    return


def check(num, string):
    logging.info(f'checking {string}... all good!')
    return True


@shared_task(bind=True, max_retries=3, default_retry_delay=0)
def add(self, num, string):
    add_complete = False
    if self.request.retries == self.max_retries:
        logging.debug(f'{string} hit max retries! returning.')
        return
    logging.info(f'{string} add : BEGIN')
    try:
        waiting(num, string)
        if string == 'tristan':
            raise Exception('raising forced tristan exception')
        result = num+num
        for i in range(result):
            time.sleep(1)
            if i % 5 == 0:
                logging.debug(f'adding {string} : {i}')
        if check(num, string):
            add_complete = True
        else:
            raise Exception('check failed')
    except Exception:
        add.retry()
    return add_complete


@shared_task
def orchestration():
    list_params = [[5, 'cuili'], [10, 'yinian'], [20, 'tristan']]
    list_of_chains = [chain(add.si(*params), add.si(*params)) for params in list_params]
    logging.debug('Running a group of tasks')
    job = group(*list_of_chains)
    result = job.apply_async(retry=True, ignore_result=False)

    group_success = False
    while not group_success:
        if result.successful():
            print('Group completed with success!')
            group_success = True
        else:
            print(f'checking success: {result.successful()}')
            time.sleep(5)

    print('whoop whoop! hit the end!')