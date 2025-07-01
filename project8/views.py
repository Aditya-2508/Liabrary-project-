from django.http import HttpResponse
from django.shortcuts import render


def about(request):
    return render(request, '.html')

def about404(request):
    return render(request, '404.html')

def blogdetail(request):
    return render(request, 'blog-detail.html')

def blog(request):
    return render(request, 'blog.html')

def booksv1(request):
    return render(request, 'books-media-detail-v1.html')

def booksv2(request):
    return render(request, 'books-media-detail-v2.html')

def booksgridv1(request):
    return render(request, 'books-media-grid-view-v1.html')

def booksgridv2(request):
    return render(request, 'books-media-grid-view-v2.html')

def bookslist(request):
    return render(request, 'books-media-list-view.html')

def cart(request):
    return render(request, 'cart.html')

def checkout(request):
    return render(request, 'checkout.html')

def contact(request):
    return render(request, 'contact.html')

def homev2(request):
    return render(request, 'home-v2.html')

def homev3(request):
    return render(request, 'home-v3.html')

def index2(request):
    return render(request, 'index-2.html')

def index(request):
    return render(request, 'index.html')

def newsdetail(request):
    return render(request, 'news-events-detail.html')

def newslist(request):
    return render(request, 'news-events-list-view.html')

def services(request):
    return render(request, 'services.html')

def signin(request):
    return render(request, 'signin.html')


