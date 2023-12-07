from django.shortcuts import render
from schedule.models import Student

# Create your views here.
def index(request):

    students = Student.objects.all()

    return render(request, 'schedule/index.html', { 'students' : students})