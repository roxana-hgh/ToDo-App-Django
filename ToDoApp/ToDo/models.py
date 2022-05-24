from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Tasks(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        editable=False,
        null=True,
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=200)
    checked = models.BooleanField(default = False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title