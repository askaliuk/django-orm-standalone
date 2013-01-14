from django.conf import settings as django_settings
import settings

django_settings.configure(DATABASES=settings.DATABASES)
from app.models import *
