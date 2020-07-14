import os

from django.core.asgi import get_asgi_application
from whitenoise.django import DjangoWhiteNoise

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "TeleMedic.settings.prod")

application = get_asgi_application()
application = DjangoWhiteNoise(application)