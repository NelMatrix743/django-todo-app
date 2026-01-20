from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    user: models.ForeignKey = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    title: models.CharField = models.CharField(max_length=200)
    description: models.TextField = models.TextField(null=True, blank=True)
    completion_status: models.BooleanField = models.BooleanField(default=False)
    datetime_created: models.DateTimeField = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return f"{self.title}|{self.completion_status}|{self.datetime_created}"


    class Meta:
        ordering: list[str] = ['completion_status']



# eosc