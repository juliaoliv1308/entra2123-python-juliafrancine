
from django.contrib import admin
from django.urls import path 
from angeline.views import *
app_name = 'angeline'

urlpatterns ={
    path('', index, name='index'),
    path('ex002', ex002, name='ex002'),
    path('contato', contato, name='contato'),
    path('ex003', ex003, name='ex003'),
    path('ex004', ex004, name='ex004'),
    path('ex005', ex005, name='ex005'),
    path('ex006', ex006, name='ex006'),
    path('ex006list', ex006list, name='ex006list')
}
