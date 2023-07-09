from django.apps import AppConfig


class ReadersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'readers'

    def ready(self):
        import readers.signals
