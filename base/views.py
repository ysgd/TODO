from django.shortcuts import render, redirect
from .models import todo

# Create your views here.
def home(request):
  todo.objs = todo.objects.all()
  data = {'todos': todo.objs}
  return render(request, 'index.html', context = data)

def create(request):
  if request.method == 'POST':
    tasks = request.POST.get('tasks')
    description = request.POST.get('description')
    status = request.POST.get('status')
    todo.objects.create(tasks=tasks,description=description,status=status)
    return redirect('home')
  return render(request, 'create.html')

def edit(request,pk):
  todo.obj = todo.objects.get(id=pk)
  if request.method == 'POST':
    tasks = request.POST.get('tasks')
    description = request.POST.get('description')
    status = request.POST.get('status')
    todo.obj.tasks = tasks
    todo.obj.description = description
    todo.obj.status = status
    todo.obj.save()
    return redirect('home')
  data = {'todo':todo.obj}
  return render(request, 'edit.html', context=data)

def delete(request,pk):
  todo.obj = todo.objects.get(id=pk)
  todo.obj.delete()
  return redirect('home')

def deleteAll(request):
  todo.obj = todo.objects.all()
  todo.obj.delete()
  return render(request, 'index.html')
  