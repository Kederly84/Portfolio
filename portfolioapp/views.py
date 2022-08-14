from django.shortcuts import render
from portfolioapp.models import Project


def home(request):
    projects = Project.objects.all()
    return render(request, 'portfolioapp/index.html', {'projects': projects})
