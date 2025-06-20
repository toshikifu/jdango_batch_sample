
from celery import shared_task


@shared_task()
def hello_world():
    print("start hello world")
    print("Hello, World!")
    print("-----"*200)
    print("end hello world")


@shared_task()
def calc(a:int, b: int) -> int:
    print("start calc")
    print(f"calc {a} + {b} = {a + b}")
    print("-----"*200)
    return a + b
