
import time
from celery import shared_task


@shared_task()
def hello_world(name: str = ""):
    print("start hello world")
    print(f"Hello, {name}")
    print("end hello world")


@shared_task()
def calc(a:int, b: int) -> int:
    print("start calc")
    print(f"calc {a} + {b} = {a + b}")
    print("-----"*200)
    return a + b

@shared_task()
def time_sleep_func(project_id: str) -> str:
    print(f"start time_sleep_func for project {project_id}")

    time.sleep(10)  # Simulating a long-running task
    message: str = f"Project {project_id} processed successfully after sleep."
    print(message)

    return message
