from django.shortcuts import render
from django.views import View
# from django.http import HttpResponse
# from django.template import loader

# Create your views here.
class Index(View):
    template_name = "app/index.html"
    
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request = request, template_name = self.template_name, context = context)
        # return HttpResponse("Hello, world. You're at the polls index.")
    
    def post(self, request, *args, **kwargs):
        pass
