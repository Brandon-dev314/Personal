from django.shortcuts import render
from .models import Project8
# Create your views here.
def portafolio(request):
    projects = Project8.objects.all()
    return render(request,"portafolio/portafolio.html",{'projects': projects})
