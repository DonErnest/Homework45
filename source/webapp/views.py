from django.http import HttpResponseBadRequest
from django.shortcuts import render, redirect, get_object_or_404

from webapp.forms import TaskForm
from webapp.models import Task, status_choices


def index_view(request):
    tasks = Task.objects.all()
    context = {
        'tasks': tasks
    }
    return render(request, 'index.html', context)


def task_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    context = {'task': task}
    return render(request, 'task_view.html', context)


def create_task_view(request):
    if request.method == 'GET':
        form = TaskForm()
        return render(request, 'create_view.html', context={
            'form': form
        })
    elif request.method == 'POST':
        form = TaskForm(data=request.POST)
        if form.is_valid():
            descr = form.cleaned_data['description']
            status = form.cleaned_data['status']
            text = form.cleaned_data['text']
            compl_date=form.cleaned_data['completed at']
            task = Task.objects.create(description=descr, status=status, completed_at=compl_date, text=text)
            return redirect('task_view', pk=task.pk)
        else:
            return render(request, 'task_view.html', context={'form':form} )


def delete(request,pk):
    task = Task.objects.get(pk=pk)
    task.delete()
    return redirect('index')