from django.db import models

# Create your models here.

class UserDetails(models.Model):
    FirstName = models.CharField(max_length=150, null=True)
    LastName = models.CharField(max_length=150, null=True)
    Email = models.CharField(max_length=100, null=True)
    Contact = models.CharField(max_length=15, null=True)
    Gender = models.CharField(max_length=15, null=True)
    image = models.FileField(null=True, blank=True)
    Hobbies = models.CharField(max_length=200, null=True)
    placeofBirth = models.CharField(max_length=100, null=True)
    placeofWork = models.CharField(max_length=150, null=True)
    profession = models.CharField(max_length=100, null=True)
    Address = models.CharField(max_length=300, null=True)
    status = models.CharField(max_length=15, null=True)
    CreationDate = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.FirstName
