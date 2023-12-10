from django.shortcuts import render
from .registration_manager import is_valid_battlenet, is_battlenet_in_database

from ow2_rank_tracker.models import Player
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
    if (not is_valid):
        return render(request, 'registration/registration_page.html')

    # Final case is to check if it is already in our database
    is_in_db = is_battlenet_in_database(input)
    print(f"Result from is_in_db..: {is_in_db}")
    if (not is_in_db):
        # add to db
        username, id = input.split('#')
        new_player = Player(nickname=username, player_id=id)
        new_player.save()
        #TODO: SEND SIGNAL THAT USER ADDED!
        return render(request, 'registration/registration_page.html')
    else:
        # TODO: SEND SIGNAL TO TEMPLATE TO INSTRUCT USER!
        return render(request, 'registration/registration_page.html')
