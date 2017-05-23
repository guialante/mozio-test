from django.apps import AppConfig


class ProvidersConfig(AppConfig):
    name = 'mozio_test.providers'
    verbose_name = "Providers"

    def ready(self):
        pass
