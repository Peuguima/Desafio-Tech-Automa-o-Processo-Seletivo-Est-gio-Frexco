from django.db import models
from uuid import uuid4


# Create your models here.


class Cadastro(models.Model):
    id_usuario = models.UUIDField(
        primary_key=True, default=uuid4, editable=False)
    login = models.CharField(max_length=255)
    senha = models.CharField(max_length=255)
    dataNascimento = models.DateField()
