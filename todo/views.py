from django.shortcuts import render, redirect,get_object_or_404
from .models import Todo
# Create your views here.

def index(request):
    todos = Todo.objects.all()
    return render(request,'index.html',{"todos":todos})

def addTodo(request):
    print(2)
    if request.method == 'GET':
        print(1)
        return redirect('/')
    else:
        print('work')

        title =request.POST.get("title")
        print('work')

        new_Todo =Todo(title = title , completed=False)
        print('work')


        new_Todo.save()




        return  redirect('/')
def update(request,id):
    todo = get_object_or_404(Todo,id=id)
    todo.completed = not todo.completed

    todo.save()
    return  redirect('/')
def delete(request,id):
    todo = get_object_or_404(Todo,id = id)
    todo.delete()
    return redirect('/')