from django.db import models
from .utils import Subjects, Year


# Create your models here.
class Student(models.Model):
    YEAR_CHOICES = [(year.name, year.value) for year in Year]
    
    
    created_on = models.DateTimeField(auto_now_add = True)
    edited_on = models.DateTimeField(auto_now = True)
    
    name = models.CharField(max_length = 200, default = "John Doe")
    year = models.CharField(max_length = 20, choices = YEAR_CHOICES, default = Year.FRESHMAN.name)
    
    def __str__(self) -> str:
        return self.name

class SubjectClass(models.Model):
    DOMAIN_CHOICES = [(domain.name, domain.value.__name__) for domain in Subjects]
    SUBJECT_CHOICES = []
    for domain in Subjects:
        for subject in domain.value:
            SUBJECT_CHOICES.append((subject.name, subject.value))
    
    created_on = models.DateTimeField(auto_now_add = True)
    edited_on = models.DateTimeField(auto_now = True)
    
    domain = models.CharField(max_length = 30, choices = DOMAIN_CHOICES, default = Subjects.CS.value.__name__)
    subject = models.CharField(max_length = 50, choices = SUBJECT_CHOICES, default = Subjects.CS.value.DL.name)
    students = models.ManyToManyField(Student, related_name = "students")
    
    
    
