from django.shortcuts import render, redirect
from .forms import TaskModelForm
from .models import TaskModel
def add_task(request):
    if request.method == 'POST':
        task_form = TaskModelForm(request.POST)
        if task_form.is_valid():
            task_form.save()
            return redirect('show_task') 
    else:
        task_form = TaskModelForm()
    
    return render(request, 'add_task.html', {'form': task_form})


def show_tasks(request):
    tasks = TaskModel.objects.all()
    return render(request, 'show_tasks.html', {'tasks': tasks})


def edit_task(request, id):
        task=TaskModel.objects.get(pk=id)
        task_form=TaskModelForm(instance=task)
        if request.method=='POST':
                task_form=TaskModelForm(request.POST, instance=task)
                if task_form.is_valid():
                        task_form.save()
                        return redirect('show_task')
                
        return render(request, 'add_task.html', {'form': task_form})

def delete_task(request, id):
        task=TaskModel.objects.get(pk=id)
        task.delete()
        return redirect('show_task')
                