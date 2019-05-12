
from django.core.management.base import BaseCommand
from django.conf import settings
import requests


class Command(BaseCommand):
    help = "promo testing"
    def handle(self, *args, **options):
        t = requests.get('http://www.mocky.io/v2/5cd84a3e3000001d2074cd6d')
        print(t.text)