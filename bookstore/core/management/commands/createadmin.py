from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.core.exceptions import ImproperlyConfigured
from django.conf import settings


class Command(BaseCommand):
    help = "Create admin user if it does not exist"

    def handle(self, *args, **options):
        if User.objects.filter(is_staff=True).count() == 0:
            user = User.objects.create_superuser(
                username="admin",
                password="admin",
                email="",
            )

            self.stdout.write(
                f"Admin user created"
            )
