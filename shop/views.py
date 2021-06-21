from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return render(request, 'shop/index.html')


def about(request):
    return HttpResponse("<h1>About Page</h1>")


def contact(request):
    return HttpResponse("<h1>Contact Page</h1>")


def tracker(request):
    return HttpResponse("<h1>Tracking Page</h1>")


def search(request):
    return HttpResponse("<h1>Search Page</h1>")


def prodView(request):
    return HttpResponse("<h1>Product View Page</h1>")


def checkout(request):
    return HttpResponse("<h1>Checkout Page</h1>")
