from django.db import models
from django.conf import settings

FILE_DIR = settings.IMAGE_FILE_PATH


class Screenshot(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to=FILE_DIR)
    source = models.CharField(max_length=50)
