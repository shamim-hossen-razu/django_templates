from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'name': 'Shamim Hossen Razu',
        'age': 28,
    }
    return render(request, 'index.html', context)
