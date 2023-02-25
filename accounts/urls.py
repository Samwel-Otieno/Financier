from django.urls import path
from . import views
app_name='accounts'

urlpatterns=[
    path('register/', views.registerview, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('reset/', views.setpassword, name='reset'),
]