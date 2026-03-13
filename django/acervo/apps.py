from django.apps import AppConfig

class AcervoConfig(AppConfig):
    name = 'acervo'

    def ready(self):
        import acervo.signals
