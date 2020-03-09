from django.db import models

# Create your models here.


class Question(models.Model):
    question = models.CharField(max_length=500)

    user = models.ForeignKey(
        'User',
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ['id']

    def __str__(self):
        return "{0} - {1}".format(self.question, self.user)


class User(models.Model):
    name = models.CharField(max_length=50)


class Answer(models.Model):
    answer = models.CharField(max_length=500)

    user = models.ForeignKey(
        'User',
        on_delete=models.CASCADE
    )

    question = models.ForeignKey(
        'Question',
        on_delete=models.CASCADE,
        default=0
    )
