from django.db import models

# Create your models here.


class Answer(models.Model):
    id = models.AutoField(primary_key=True)
    answer = models.CharField(max_length=200, default="")
