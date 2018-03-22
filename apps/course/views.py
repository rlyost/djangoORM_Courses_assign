from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from time import gmtime, strftime
from .models import Course, Description

def index(request):
    return render(request, 'index.html', { "courses": Course.objects.all() })

def create(request):
    if request.method == "POST":
        Course.objects.create(name=request.POST['name'])
        Description.objects.create(course=Course.objects.last(), desc=request.POST['desc'])
    return redirect('in')

def destroy(request, id):
    context = {
        'courses': Course.objects.get(id=id),
        'desc': Description.objects.get(course=Course.objects.get(id=id))
    }
    return render(request, 'destroy.html', context)

def end(request, id):
    print id
    destroyit = Course.objects.get(id=id)
    destroyit.delete()
    return redirect('/')