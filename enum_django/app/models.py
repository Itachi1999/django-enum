from django.db import models


# Create your models here.
class Student(models.Model):
    created_on = models.DateTimeField(auto_now_add = True)
    edited_on = models.DateTimeField(auto_now = True)
    
    name = models.CharField(max_length = 200, default = "John Doe")
