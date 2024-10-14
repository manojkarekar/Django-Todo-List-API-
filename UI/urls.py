from django.urls import path
from .views import *

urlpatterns = [
    path("",index,name="Home"),
    path("add-todo/",add_todo_view,name="add_todo"),
]
