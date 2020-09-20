import time

from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError


class Command(BaseCommand):
    """Django Command to wait for db connection"""

    def handle(self, *args, **options):
        self.stdout.write("Database Loading...")
        db_conn = None
        while not db_conn:
            try:
                db_conn = connections["default"]
            except OperationalError:
                self.stdout.write("Database unavailable, Waiting for retry...")
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS("Database Connected!"))
