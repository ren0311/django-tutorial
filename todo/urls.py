from django.urls import path

from . import views

urlpatterns = [
    path("todo", views.list, name="todo"),
    path("edit", views.edit, name="edit"),
    path("todo2", views.list2, name="todo2"),
    path("edit2", views.edit2, name="edit2"),
]
