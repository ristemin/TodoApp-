from django.shortcuts import render, redirect
from . models import *
from . forms import *


def index(request):
    tasks = Task.objects.all()

    form = TaskForm()

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'tasks': tasks, 'form':form}
    return render(request, 'blog/list.html', context)



def updateTask(request, id):
    task = Task.objects.get(id=id)

    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}

    return render(request, 'blog/update_task.html', context)

def deleteTask(request, id):
    item = Task.objects.get(id=id)
    if request.method == 'POST':
        item.delete()
        return redirect('/')
    context = {'item':item}
    return render(request, 'blog/delete.html', context)
