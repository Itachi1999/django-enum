from django.shortcuts import render
from django.views import View
from django.contrib import messages
from .models import (
    Year,
    Subjects,
    Student,
    SubjectClass
)
# from django.http import HttpResponse
# from django.template import loader

# Create your views here.
class Index(View):
    template_name = "app/index.html"
    
    def get(self, request, *args, **kwargs):
        subjects = {}
        for domain in Subjects:
            subjects[domain.name] = list(domain.value)
        
        print(subjects)
             
        context = {
            "year": list(Year),
            "subjects": subjects
        }
        return render(request = request, template_name = self.template_name, context = context)
        
    
    def post(self, request, *args, **kwargs):
        name = request.POST.get("name")
        year = request.POST.get("year")
        domain, subject = request.POST.get("subject").split("-")
        
        print(name, year, domain, subject)
        
        student_obj = Student.objects.create(name = name, year = year)
        
        subject_class, created = SubjectClass.objects.get_or_create(domain = domain, subject = subject)
        subject_class.students.add(student_obj)
        
        messages.add_message(request, messages.SUCCESS, message = f"Student {name} has been added")
        
        subjects = {}
        for domain in Subjects:
            subjects[domain.name] = list(domain.value)
        
        print(subjects)
             
        context = {
            "year": list(Year),
            "subjects": subjects
        }
        
        return render(request = request, template_name = self.template_name, context = context)