import uuid
from django.db import models


class Book(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    title = models.CharField(max_length=255)
    pages = models.IntegerField()
    author = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title
