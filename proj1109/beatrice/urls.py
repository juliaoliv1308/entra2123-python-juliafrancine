#beatrice urls.py
from django.urls import path 
from beatrice.views import index

app_name = 'beatrice'


urlpatterns =[
    path('', index, name='index'),   
    #path('ex001/', ex001, name='ex001'),
]
