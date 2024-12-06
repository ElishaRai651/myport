from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'index.html')
 
def resume(request):
   return render(request, 'resume.html')
 
def projects(request):
     return render(request,'projects.html')
 
def contact(request):
    return render(request, 'contact.html')