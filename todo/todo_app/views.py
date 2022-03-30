from django.shortcuts import render, redirect

# Create your views here.
from forms import Todoform
from todo_app.models import Task


def fun1(request):
    if request.method == 'POST':
        name = request.POST['name']
        priority = request.POST['priority']
        date = request.POST['date']
        task = Task(name=name, priority=priority, date=date)
        task.save()
    tasks = Task.objects.all()
    return render(request, 'home.html', {'task1': tasks})


def done(request, id):
    tas = Task.objects.get(id=id)
    if request.method == 'POST':
        tas.delete()
        return redirect('/')
    return render(request, 'done.html')


def update(request, tid):
    tas = Task.objects.get(id=tid)

    form = Todoform(request.POST or None, instance=tas)
    if form.is_valid():
        form.save()
        return redirect('/')

    return render(request, 'update.html', {'key': form, 'key1': tas})
