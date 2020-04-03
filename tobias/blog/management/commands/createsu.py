"""tobias.fyi :: Management commands

Adds a command to create the superuser.
"""

import os

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = "Creates a superuser with environment var password."

    def handle(self, *args, **options):
        if not User.objects.filter(username="fyiadmin").exists():
            User.objects.create_superuser(
                "fyiadmin", "hi@tobias.fyi", os.environ.get("SU_PASSWORD")
            )
