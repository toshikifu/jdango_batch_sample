from django.core.management.base import BaseCommand
from polls.tasks import hello_world

class Command(BaseCommand):
    def handle(self, *args, **options):
        print("====== start =======")

        hello_world.apply_async(args=(options['name'],))

        print("====== end =======")

    def add_arguments(self, parser):
        parser.add_argument(
            '--name',
            type=str,
            help='Name to greet',
        )
