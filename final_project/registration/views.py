from django.shortcuts import render
from .registration_manager import is_valid_battlenet
# Create your views here.
def registration_page(request):
    input = request.POST.get('battle.net_id')

    # First case is that there was no input
    if (input == ""):
        print("User did not enter anything!")
        # TODO: SEND SIGNAL TO TEMPLATE TO INSTRUCT USER!
        return render(request, 'registration/registration_page.html')
    
    # Second case is that their input does not resemble a valid battletag
    # as in https://eu.battle.net/support/en/article/26963
    is_valid = is_valid_battlenet(input)
    print(f"Result from is_valid..: {is_valid}")

    return render(request, 'registration/registration_page.html')
