import os

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Creates an admin user non-interactively if it doesn't exist"

    def add_arguments(self, parser):
        parser.add_argument("--username", help="Admin's username")
        parser.add_argument("--email", help="Admin's email")
        parser.add_argument("--password", help="Admin's password")

    def handle(self, *args, **options):
        user = get_user_model()
        username = options.get("username") or os.getenv("DJANGO_SUPERUSER_USERNAME")
        email = options.get("email") or os.getenv("DJANGO_SUPERUSER_EMAIL")
        password = options.get("password") or os.getenv("DJANGO_SUPERUSER_PASSWORD")
        if not user.objects.filter(username=username).exists():
            user.objects.create_superuser(
                username=username, email=email, password=password
            )
