from django.shortcuts import render
from django.shortcuts import redirect
from .overfast_api import populate_db_with_player_ranks
from .models import Player

def rank_tracker(request):
    players = Player.objects.all()
    if request.method == 'POST':
        should_update = request.POST.get('update_rank_info')
        if (should_update == "update_ranks"):
            populate_db_with_player_ranks()
            print(should_update)
    return render(request, 'ow2_rank_tracker/rank_tracker.html', {'players': players, 'num_players': players.count()})

# Create your views here.
def index(request):
    #populate_db_with_player_ranks()
    return render(request, 'ow2_rank_tracker/index.html',)

                    