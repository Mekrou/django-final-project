from django.shortcuts import render

# Create your views here.
def registration_page(request):
    return render(request, 'registration/registration_page.html')
