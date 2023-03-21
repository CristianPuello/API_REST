from django.db import models
from .choices import JOKER_TYPE_CHOICES


class Jokes(models.Model):
    joke = models.CharField(unique=True, max_length=100)
    joker_type = models.CharField(max_length=5, choices=JOKER_TYPE_CHOICES,default='NONE')

    def __str__(self):
        return self.joke
    

class Profile(models.Model):
    name = models.CharField(max_length=40, null=False, unique=True )
    document = models.IntegerField(max_length=12, null=False, unique=True)

    def __str__(self):
        return self.name
    

class JokeAssignment(models.Model):
    profile = models.ForeignKey(Profile, on_delete = models.CASCADE)
    joke = models.ForeignKey(Jokes, on_delete= models.CASCADE)
    assigned_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.profile.name} - {self.joke.joke}"