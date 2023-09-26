
from django.contrib import admin
from django.urls import path 
from angeline.views import index, ex002, contato, ex003
app_name = 'angeline'

urlpatterns ={
    path('', index, name='index'),
    path('ex002', ex002, name='ex002'),
    path('contato', contato, name='contato'),
    path('ex003', ex003, name='ex003'),
    
}
