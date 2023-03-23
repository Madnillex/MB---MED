from django.shortcuts import render

from .models import Course, Teachers


def index(request):
    courses = Course.objects.all()
    teachers = Teachers.objects.all()
    context = {
        'title': 'MB-MED',
        'courses': courses,
        'teachers': teachers
    }
    return render(request, 'blog/index.html', context)
