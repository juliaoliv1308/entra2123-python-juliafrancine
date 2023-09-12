
from django.contrib import admin
from django.urls import path 
from angeline.views import index, ex002

urlpatterns ={
    path('', index, name='index'),
    path('ex002', ex002, name='ex002'),
}
