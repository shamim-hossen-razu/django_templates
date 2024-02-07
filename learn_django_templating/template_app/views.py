from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'title': 'Home',
        'content': 'Welcome to the homepage.'
    }
    return render(request, 'index.html', context)
