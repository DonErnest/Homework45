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
            compl_date = form.cleaned_data['completed_at']
            task = Task.objects.create(description=descr, status=status, completed_at=compl_date, text=text)
            return redirect('task_view', pk=task.pk)
        return render(request, 'create_view.html', context={'form': form} )


def update_task_view(request,pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'GET':
        form = TaskForm(data={'description': task.description, 'status': task.status,
                              'text': task.text, 'completed_at': task.completed_at })
        return render(request, 'update_view.html', context={'form': form, 'task': task})
    elif request.method == 'POST':
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task.description = form.cleaned_data['description']
            task.status = form.cleaned_data['status']
            task.text = form.cleaned_data['text']
            task.completed_at = form.cleaned_data['completed_at']
            task.save()
            return redirect('task_view', pk=task.pk)
        else:
            return render(request, 'update_view.html', context={'form':form, 'task': task})


def delete(request,pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'GET':
        form = TaskForm(data={'description': task.description, 'status': task.status,
                              'text': task.text, 'completed_at': task.completed_at})
        return render(request, 'delete_confirmation.html', context={'form':form,'task':task})
    elif request.method == 'POST':
        task.delete()
    return redirect('index')


def delete_multiple(request, *args, **kwargs):
    tasks=[]
    if request.method == 'GET':
        keys = dict(request.GET)['delete_check']
        for key in keys:
            tasks.append(Task.objects.get(pk=int(key)))
        return render(request, 'delete_multiple.html',context={'tasks': tasks, 'keys': keys})
    elif request.method == 'POST':
        keys = dict(request.POST)['delete_check']
        for key in keys:
            del_task = Task.objects.get(pk=int(key))
            del_task.delete()
        return redirect('index')
