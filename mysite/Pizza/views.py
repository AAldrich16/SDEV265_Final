from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def menu(request):
    return render(request, 'menu.html', {})

def locations(request):
    return render(request, 'Locations.html', {})

def cart(request):
    return render(request, 'Cart.html', {})