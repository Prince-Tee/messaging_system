from celery import Celery

app = Celery('worker', broker='amqp://guest:guest@rabbitmq//', backend='rpc://')

app.conf.task_routes = {
    'app.tasks.*': {'queue': 'email'}
}
