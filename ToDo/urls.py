from django.urls import path
from . import views
urlpatterns = [
    path('index/<uid>', views.index, name="index"),
    path('add/<uid>', views.addToDo, name='add'),
    path('complete/<todo_id><uid>', views.completeToDo, name='complete'),
    path('deleteCompleted/<uid>', views.deleteCompleted, name='deleteCompleted'),
    path('deleteAll/<uid>', views.deleteAll, name='deleteAll'),
    path('update/<uid>', views.update, name='update'),
    path('update_add/<todo_id>', views.update_add, name='update_add'),
    path('updatetodo/<todo_id>', views.updatetodo, name='updatetodo'),
    path('register', views.register, name='register'),
    path('', views.login, name='login'),
    path('register_redirect', views.register_redirect, name='register_redirect'),
    path('login_redirect', views.login_redirect, name='login_redirect'),
    path('logout', views.logout, name='logout')

]