from django.db import models


class Party(models.Model):
    name = models.CharField(max_length=64)
    ideology = models.CharField(max_length=64)
    chairs_count = models.IntegerField()


class President(models.Model):
    name = models.CharField(max_length=64)
    age = models.IntegerField()
    sex = models.BooleanField(choices=[(True, 'male'), (False, 'female'), ], default=True)
    party = models.ForeignKey(Party, on_delete=models.CASCADE)

    def __repr__(self):
        return {'name': self.name,
                'age': self.age,
                'sex': self.sex,
                'party': self.party
                }

        # Create your models here.
