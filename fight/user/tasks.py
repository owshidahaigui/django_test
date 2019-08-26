from celery import Celery

app=Celery('dahaigui',
           broker='redis://@127.0.0.1/1')

@app.task
def task_test():
    print('task is runing !!')