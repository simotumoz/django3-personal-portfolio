from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Project
from .models import Contact


def home(request):
    projects = Project.objects.all()

    if request.method == 'POST':

        name = request.POST.get('name')
        surname = request.POST.get('surname')
        email = request.POST.get('email')
        text = request.POST.get('text')
        contact = Contact(name=name, surname=surname, email=email, text=text)
        contact.save()

    return render(request, 'portfolio/home.html', {'projects': projects})