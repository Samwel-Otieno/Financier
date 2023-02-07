from django.urls import path
from . import views

app_name='web'

urlpatterns=[
    path('index/', views.index, name='index'),
]