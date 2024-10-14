from django.urls import path
from .views import *

urlpatterns = [
    path("add_todo/",add_todo),
    path("view_todo/",view_todo),
    path("delete_todo/<int:pk>/",delete_todo),
    path("update_todo/<int:pk>/",update_todo),


    path('register/', register, name='register'),
    path('login/', login, name='login'),

]
