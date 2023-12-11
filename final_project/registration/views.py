from django.shortcuts import render
from .registration_manager import is_valid_battlenet, is_battlenet_in_database
from django.db.utils import IntegrityError


from ow2_rank_tracker.models import Player
# Create your views here.
def registration_page(request):
    input = request.POST.get('battle.net_id')

    # First case is that there was no input
    if (input == "" or input == None):
        print("User did not enter anything!")
        return render(request, 'registration/registration_page.html', {'response': 'Enter a username!'})
    
    # Second case is that their input does not resemble a valid battletag
    # as in https://eu.battle.net/support/en/article/26963
    is_valid = is_valid_battlenet(input)
    print(f"Result from is_valid..: {is_valid}")
    if (not is_valid):
        return render(request, 'registration/registration_page.html', {'response': 'Invalid username!'})

    # Final case is to check if it is already in our database
    is_in_db = is_battlenet_in_database(input)
    print(f"Result from is_in_db..: {is_in_db}")
    if (not is_in_db):
        # add to db
        username, id = input.split('#')
        new_player = Player(nickname=username, player_id=id)

        # The below check is if a battle.net ID exists in our DB, but username
        # was unique. This can happen when case in the name is different
        try:
            new_player.save()
        except IntegrityError as e:
            return render(request, 'registration/registration_page.html', {'response': 'That battle.net ID is already being tracked!'})
        return render(request, 'registration/registration_page.html', {'response': 'User successfully added!'})
    else:
        return render(request, 'registration/registration_page.html', {'response': 'That user is already being tracked!'})
