from django.http import HttpResponse
from django.shortcuts import render
from django import forms

tasks=["gym","game","swim"]

# Create your views here.
class newTaskforms(forms.Form):
    task=forms.CharField(label="New task")



def index(request):
    return render(request,"index.html",{
        "tasks":tasks
    })

def add(request):
    if request.method=='POST':
        form=newTaskforms(request.POST)
        if form.is_valid():
            task=form.cleaned_data["task"]
            tasks.append(task)
        else:
            return render(request,"add.html",{
                "form":form
            })
    return render(request,"add.html",{
        "form":newTaskforms()
    })