from django.db import models

# Create your models here.

class student(models.Model):
    name=models.CharField(max_length=30)
    age=models.IntegerField()
    subject=models.CharField(max_length=20)

    def __str__(self):
        return self.name

class regmodel(models.Model):
    Name = models.CharField(max_length=40)
    Phone = models.IntegerField()
    Email = models.EmailField()
    Password = models.CharField(max_length=30)


    def __str__(self):
        return self.Name