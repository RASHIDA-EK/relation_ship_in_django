from django.db import models
from django.contrib.auth.models import User

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthdate = models.DateField()
    bio = models.TextField()

    def __str__(self):
        return self.user.username


# Create your models here.




# Create your models here.
