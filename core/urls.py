from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('author_create',views.author_create,name='author_create'),
    path('author_get',views.author_get,name='author_get'),
    path('book_create',views.book_create,name='book_create'),
    path('author_delete/<author_id>',views.author_delete,name='author_delete')

]