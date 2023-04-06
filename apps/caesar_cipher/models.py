from django.db import models


class MessageModel(models.Model):
    text = models.TextField(max_length=250)
    key_step = models.IntegerField(default=0, blank=True, null=True)
