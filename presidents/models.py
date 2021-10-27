from django.db import models


class Party(models.Model):
    name = models.CharField(max_length=64)
    ideology = models.CharField(max_length=64)
    chairs_count = models.IntegerField()


class President(models.Model):
    name = models.CharField(max_length=64)
    age = models.IntegerField()
    sex = models.BooleanField(choices=["male", "female"], default="male")
    party = models.ForeignKey(Party, on_delete=models.CASCADE)

# Create your models here.
