from django.shortcuts import render
from .registration_manager import is_valid_battlenet, is_battlenet_in_database
from ow2_rank_tracker.overfast_api import update_player_ranks
from django.db.utils import IntegrityError


from ow2_rank_tracker.models import Player
# Create your views here.
def registration_page(request):
    input = request.POST.get('battle.net_id')
    submit_button = request.POST.get('submit-button')

    # This is to prevent prompting "Enter a username"
    # upon a user's initial visit.
    # We only want to display feedback if they click the submit button
    if (submit_button != "submit_was_clicked"):
            return render(request, 'registration/registration_page.html')

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
        # IntegrityError gets raised because our ID is marked as unique in our model, as it should be!
        try:
            new_player.save()
        except IntegrityError as e:
            return render(request, 'registration/registration_page.html', {'response': 'That battle.net ID is already being tracked!'})
        
        # update their rank data in database
        update_player_ranks(input)
        return render(request, 'registration/registration_page.html', {'response': 'User successfully added!'})
    else:
        return render(request, 'registration/registration_page.html', {'response': 'That user is already being tracked!'})
