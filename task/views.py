from django.shortcuts import render, redirect
from .forms import TaskModelForm

def add_task(request):
    if request.method == 'POST':
        task_form = TaskModelForm(request.POST)
        if task_form.is_valid():
            task_form.save()
            return redirect('add_task') 
    else:
        task_form = TaskModelForm()
    
    return render(request, 'add_task.html', {'form': task_form})
