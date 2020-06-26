from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Todolist
from django.utils import timezone
from datetime import datetime
from django.contrib import messages


# Create your views here.

def index(request):
    TodaData = Todolist.objects.all()
    return render(request, 'Index.html', {'TodaData': TodaData})
    # return HttpResponse("haoooo")


def AddItem(request):
    if request.method == "POST":
        currentdate = timezone.now()
        txtdata = request.POST["content"]
        Todolist.objects.create(created_date=currentdate, text=txtdata)
        return render(request, 'Add.html', {'msg': 'Succesfully Inserted the Item'})
        # return messages.success(request,'Add.html','Succesfully Inserted the Item')
        # return HttpResponse('<h1> Successfully Created</h1>')
        # return HttpResponseRedirect("/ToDoList/")
    return render(request, 'Add.html', )


def DeleteItem(request, todo_list):
    Todolist.objects.get(list_id=todo_list).delete()
    return HttpResponseRedirect("/ToDoList/")


def EditItem(request, todo_list):
    dataedit = Todolist.objects.get(list_id=todo_list)
    return render(request, 'Details.html', {'dataedit': dataedit})


def UpdateItem(request, todo_list):
    if request.method == 'POST':
        currentdate = timezone.now()
        txtdata = request.POST["content"]
        print(txtdata)
        Todolist.objects.filter(list_id=todo_list).update(created_date=currentdate, text=txtdata)
        # Todolist.objects.create(created_date=currentdate, text=txtdata)
        # Todolist.objects.select_for_update(created_date=currentdate, text=txtdata).filter(list_id=todo_list)
        # Todolist.objects.get(list_id=todo_list).update_or_create(created_date=currentdate, text=txtdata)
        return HttpResponseRedirect("/ToDoList/")
    return HttpResponseRedirect("/ToDoList/")
