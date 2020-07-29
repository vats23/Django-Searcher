from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect
from . import forms
from . import models

# Create your views here.
def home(request):
    return render(request,"searcher/home.html")

def register(request):
    if request.method == "POST":
        form = forms.register(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("searcher:finder"))
        else:
            print(form.errors)
    else:
        form = forms.register()
    return render(request,"searcher/register.html",{'form':form})

def finder(request):
    find = False
    t = None
    submitted = False
    if request.method == "POST":
        submitted = True
        form = forms.finder(request.POST)
        if form.is_valid():
            x= form.cleaned_data['by_location']
            x.lower()
            print(x)
            try:
                t = models.Person.objects.filter(location=x)
            except models.Person.DoesNotExist:
                t = None
        else:
            print(form.errors)
    else:
        form =forms.finder()
    return render(request,"searcher/finder.html",{"form":form,"ans":t,'submitted':submitted})
