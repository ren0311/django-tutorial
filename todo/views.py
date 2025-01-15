from django.shortcuts import render

from django.http import HttpResponse

from todo import models


def list(request):
    new_todo = models.Todo()
    new_todo.todo_title = "New Todo"
    new_todo.save()

    all_todo = models.Todo.objects.all()
    context = {"todos"}
    return HttpResponse("list")


def edit(request):
    return HttpResponse("edit")


def list2(request):
    return HttpResponse("list2")


def edit2(request):
    return HttpResponse("edit2")
