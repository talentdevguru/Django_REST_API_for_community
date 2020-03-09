from django.db import models
# from answer.models import Answer
# from user.models import User
# Create your models here.


# class Question(models.Model):
#     id = models.AutoField(primary_key=True)
#     question = models.CharField(max_length=500)
#     answers = models.ForeignKey(
#         'Answer',
#         on_delete=models.DO_NOTHING,
#     )
#     createdBy = models.ForeignKey(
#         'User',
#         on_delete=models.DO_NOTHING
#     )

class Garden(models.Model):
    name = models.CharField(max_length=200)


class Vegetable(models.Model):
    name = models.CharField(max_length=100)

    garden = models.ForeignKey('Garden',
                               on_delete=models.DO_NOTHING
                               )
