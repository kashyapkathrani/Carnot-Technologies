from django.apps import AppConfig
from . import utils

class ApisConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'APIs'
    def ready(self):
        utils.processCSV()
