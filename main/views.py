from django.shortcuts import render, HttpResponse, redirect
from .models import ToDo, Books

def homepage(request):
    return render(request, "index.html")



def test(request):
    todo_list = ToDo.objects.all()
    return render(request, "test.html", {"todo_list": todo_list})


def second(request):
    return HttpResponse("test 2 page")

def third(request):
    return HttpResponse("This is page test3")

def first(request):
    return render(request, "index1.html")

def books(request):
    books = Books.objects.all()
    return render(request, "books.html", {"books": books})
    
def add_todo(request):
    form = request.POST
    text = form["todo_text"]  
    todo = ToDo(text=text)
    todo.save()
    return redirect(test)

def delete_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.delete()
    return redirect(test)

def mark_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_favorite = True
    todo.save()
    return redirect(test)

def unmark_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_favorite = False
    todo.save()
    return redirect(test)

def close_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_closed = not todo.is_closed
    todo.save()
    return redirect(test)

def add_book(request):
    form = request.POST
    
    book.save()
    return redirect(books)

