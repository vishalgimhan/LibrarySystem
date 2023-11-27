"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', home),
    path('home', home),
    path('readers', readers_tab),
    path('save', save_student),
    path('readers/add', save_reader),
    path('books', books_tab),
    path('mybag', mybag_tab),
    path('get_reader/', get_reader, name="get_reader"),
    path('returns', returns_tab),
    path('search_book/', search_books, name='search_books'),
    path('search_reader/', search_reader, name='search_reader'),
]



