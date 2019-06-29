from django.shortcuts import render

from .models import Lecture

def lectures(request):
    lectures = Lecture.objects.all()
    return render(request, 'lectures.html', {'lectures':lectures})
