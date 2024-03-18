from django.db import models

# Create your models here.
# translator/models.py


class UploadedAudio(models.Model):
    audio_file = models.FileField(upload_to='uploads/')
    # Add any other fields you need
