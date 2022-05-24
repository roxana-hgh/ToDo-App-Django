from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import Tasks
import datetime

def landing(request):
    return render(request, 'ToDo/landing.html')


@login_required(login_url = 'login')
def tasks(request):
    tasks = Tasks.objects.filter(user = request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('tasks')
    else:
        form = TaskForm()

    currentTime = datetime.datetime.now()
    date = currentTime.strftime("%A, %B %d").lstrip("0").replace(" 0", " ")
    return render(request, 'ToDo/list.html', {'form' : form, 'tasks': tasks , 'date': date})



@login_required(login_url = 'login')
def update_task(request,pk):
    task = Tasks.objects.get(id=pk)
    form = TaskForm(request.POST or None, instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('tasks')

    context = {'form': form, 'item': task}
    return render(request,'ToDo/update.html',context)

@login_required(login_url = 'login')
def delete(request,pk):
    task = Tasks.objects.get(id=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('tasks')

    context = {'item': task}
    return render(request,'ToDo/delete.html',context)



