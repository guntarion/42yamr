from django.apps import AppConfig


class YamrquestionsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'yamrquestions'

    def ready(self):
        import yamrquestions.signals