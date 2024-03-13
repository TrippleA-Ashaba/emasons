import uuid

from auditlog.registry import auditlog
from author.decorators import with_author
from django.contrib.auth.models import AbstractUser
from django.db import models
from django_extensions.db.models import TimeStampedModel


@with_author
class User(AbstractUser, TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email


auditlog.register(User)
