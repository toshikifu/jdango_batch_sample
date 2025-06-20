import time
from django.core.management.base import BaseCommand

from celery.result import AsyncResult

from polls.tasks import time_sleep_func

class Command(BaseCommand):
    def handle(self, *args, **options):
        project_id: str = "0001"
        task: AsyncResult = time_sleep_func.delay(project_id)
        print("task status:", task.status)

        task_id: str = task.id
        print("task id:", task_id)

        task_1: AsyncResult = AsyncResult(task_id)
        while not task.ready():
            time.sleep(1)
            print("task status:", task.status)
            task_1 = AsyncResult(task_id)
