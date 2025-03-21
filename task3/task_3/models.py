from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ProfileModel(models.Model):
    Name = models.CharField(max_length=20)
    Address = models.CharField(max_length=40)
    Phone = models.IntegerField()
    Age = models.IntegerField()

    def __str__(self):
        return self.Name

class Profile2Model(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    address = models.CharField(max_length=40)
    phone = models.IntegerField()
    age = models.IntegerField()
    upload = models.ImageField(upload_to='profilepics/', blank=True, null=True)

    def __str__(self):
        return self.first_name
    
class Author(models.Model):
    Name = models.CharField(max_length=30)    
    #could add more fields
    def __str__(self):
        return self.Name
    
class Gener(models.Model):
    gener = models.CharField(max_length=30)    
    #could add more fields
    def __str__(self):
        return self.gener       
    
class Book(models.Model):
    Title = models.CharField(max_length=40)
    Author = models.ForeignKey(Author,on_delete=models.CASCADE)
    Gener = models.ManyToManyField(Gener)    
    Publish_date = models.DateField()
    Image = models.ImageField(upload_to='Book/', null=True , blank=True)
    def __str__(self):
        return self.Title    