
from django.contrib import admin
from django.urls import path 
from angeline.views import index, ex002, contato

urlpatterns ={
    path('', index, name='index'),
    path('ex002', ex002, name='ex002'),
    path('contato', contato, name='contato')
    
}
