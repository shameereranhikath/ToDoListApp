from django.urls import path
from . import views

app_name = 'Todourls'
urlpatterns = [

    path('', views.index, name='index'),
    path('AddItem/', views.AddItem, name='AddItem'),
    path('DeleteItem/<int:todo_list>/', views.DeleteItem, name='Delete'),
    path('AddItempage/', views.AddItem, name='AddItempage'),
    path('EditItem/<int:todo_list>/', views.EditItem, name='Edit'),
    path('UpdateItem/<int:todo_list>/', views.UpdateItem, name='Update'),
]
