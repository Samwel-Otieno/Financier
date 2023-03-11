from django.urls import path
from . import views

app_name='blog'

urlpatterns=[
    path('blog/', views.blog, name='blogs'),
    path('create_blog/', views.create_blog, name='create'),
    path('comments/', views.comments, name='comments'),
    path('generatepdf/', views.generatepdf, name='generatepdf'),
]