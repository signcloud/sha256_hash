from django.db import models


class HashesModel(models.Model):
    file = models.CharField(max_length=255)
    hash = models.CharField(max_length=65)

    def __str__(self):
        return self.file + ' ' + self.hash
