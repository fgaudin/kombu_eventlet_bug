from celery import Celery


app = Celery('tasks', broker='amqp://guest:guest@localhost:5672/')

app.conf.update(
    broker_pool_limit=0,
)


@app.task
def add(x, y):
    return x + y


def app(environ, start_response):
    data = b"Hello, World!\n"
    add.delay(1,2)
    start_response("200 OK", [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(data)))
    ])
    return iter([data])
