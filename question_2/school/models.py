from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Creating profile model using OneToOneField, It will be linked with the corresponding user
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    studclass = models.CharField(max_length=10, null=True, blank=True)
    section = models.CharField(max_length=10, null=True, blank=True)
    stream = models.CharField(max_length=50, null=True, blank=True)
    rollno = models.CharField(max_length=100, null=True, blank=True)
    subject = models.CharField(max_length=50, null=True, blank=True)
    classtaught = models.CharField(max_length=10, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return str(self.user)

# Creating contact model
class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=14)
    email = models.CharField(max_length=100)
    content = models.TextField()
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return f"Message from {self.name}"