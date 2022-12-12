from django.db import models

class EmojiModels(models.Model):
    emoji = models.CharField(max_length=10)
    nama = models.CharField(max_length=20)
    keterangan = models.TextField()