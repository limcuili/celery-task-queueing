from app.celery import app

@app.task
def hello_world():
    print('Hello World... Sundays, eh')