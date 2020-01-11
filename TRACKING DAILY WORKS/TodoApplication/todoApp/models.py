from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class author(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_picture = models.FileField()

    def __str__(self):
        return self.name.username


class post(models.Model):
    post_author = models.ForeignKey(author, on_delete=models.CASCADE)
    item = models.CharField(max_length=200)
    Date = models.DateField("Date(mm/dd/yy)")
    completed = models.BooleanField(default = False)

    def __str__(self):
        return self.item + ' | ' + str(self.Date) + ' | ' + str(self.completed)