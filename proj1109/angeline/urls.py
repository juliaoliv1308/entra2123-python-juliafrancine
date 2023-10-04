from django.contrib import admin
from django.urls import path 
from angeline.views import ex002, index, ex003, ex004, ex005, ex007, ex007_add, ex007_remove, contato

app_name = 'angeline'

urlpatterns = [
    path('', index, name='index'),
    path('ex002/', ex002, name='ex002'),
    path('contato/', contato, name='contato'),
    path('ex003/', ex003, name='ex003'),
    path('ex004/', ex004, name='ex004'),
    path('ex005/', ex005, name='ex005'),
    path('ex007/', ex007, name= 'ex007'),
    path('ex007/remove/<int:id_produto>/', ex007_remove, name='ex007_remove'),
    path('ex007/add/', ex007_add, name='ex007_add'),
]
