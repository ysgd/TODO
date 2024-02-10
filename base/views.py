from django.shortcuts import render
from .models import todo

# Create your views here.
def home(request):
  todo.objs = todo.objects.all()
  data = {'todos': todo.objs}
  return render(request, 'index.html', context = data)

def create(request):
  if request.method == 'POST':
    tasks = request.POST.get('tasks')
    desc = request.POST.get('desc')
    status = request.POST.get('status')
    todo.objects.create(tasks=tasks,desc=desc,status=status)
  return render(request, 'create.html')