from django.shortcuts import render

# Create your views here.
def registration_page(request):
    input = request.POST.get('battle.net_id')
    print(input)
    print(f'type: {type(input)}')
    return render(request, 'registration/registration_page.html')
