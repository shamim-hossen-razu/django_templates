from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'name': 'Shamim Hossen Razu',
        'age': 28,
        'student': True,
        'professional': False,
        'subjects': ['Math', 'Physics', 'Chemistry', 'Biology', 'English'],
        'marks': {'Math': 80, 'Physics': 85, 'Chemistry': 90, 'Biology': 95, 'English': 100},
        }
    return render(request, 'index.html', context)
