from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_page(request):
    context = {}
    return render(request, "spacr/index.html", context)

def search(request):
    context = {}
    return render(request, "spacr/search.html", context)

def list(request):
    context = {}
    return render(request, "spacr/list.html", context)
