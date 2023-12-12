from django.shortcuts import render

# Create your views here.
def map_picker(request):
    return render(request, 'map_picker/map_picker.html')