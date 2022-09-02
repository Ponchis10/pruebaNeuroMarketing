from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return render(request, 'neuroMarketingApp/home.html')

def creditos(request):
    return render(request, 'neuroMarketingApp/creditos.html')