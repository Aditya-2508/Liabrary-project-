"""
URL configuration for project8 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', views.about, name='about'),
    path('about404/', views.about404, name='about404'),
    path('blog-detail/', views.blogdetail, name='blogdetail'),
    path('blog/', views.blog, name='blog'),
    path('books-media-detail-v1/', views.booksv1, name='booksv1'),
    path('books-media-detail-v2/', views.booksv2, name='booksv2'),
    path('books-media-grid-view-v1/', views.booksgridv1, name='booksgridv1'),
    path('books-media-grid-view-v2/', views.booksgridv2, name='booksgridv2'),
    path('books-media-list-view/', views.bookslist, name='bookslist'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('contact/', views.contact, name='contact'),
    path('home-v2/', views.homev2, name='homev2'),
    path('home-v3/', views.homev3, name='homev3'),
    path('index-2/', views.index2, name='index2'),
    path('', views.index, name='index'),
    path('news-events-detail/', views.newsdetail, name='newsdetail'),
    path('news-events-list-view/', views.newslist, name='newslist'),
    path('services/', views.services, name='services'),
    path('signin/', views.signin, name='signin'),
    path('index.html', views.index, name='index'),
    path('index-2.html', views.index2, name='index2'),
    path('home-v2.html', views.homev2, name='homev2'),
    path('home-v3.html', views.homev3, name='homev3'),
    

   
]
