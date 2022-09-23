from django.apps import AppConfig


class TweetsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tweets'

class PicturesConfig(AppConfig):
    name = 'pictures'