from django.shortcuts import render


def index(request):
    
    return render(request, 'App1/index.html')

def about(request):
    
    return render(request, 'App1/about.html')