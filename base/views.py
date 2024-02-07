from django.shortcuts import render
from .models import todo

# Create your views here.
def home(request):
  todo.objs = todo.objects.all()
  data = {'todos': todo.objs}
  return render(request, 'index.html', context = data)
