from django.shortcuts import render
from .overfast_api import get_player_ranks
from .models import Player

players = Player.objects.all()

def rank_tracker(request):
    return render(request, 'ow2_rank_tracker/rank_tracker.html')

# Create your views here.
def index(request):
    #populate_db_with_player_ranks()
    return render(request, 'ow2_rank_tracker/index.html')


def populate_db_with_player_ranks():
    for player in players:
        player_id = player.nickname + "-" + player.player_id
        
        player_ranks = get_player_ranks(player_id)
        if (player_ranks):
            for rank in player_ranks:
                if (rank == 'tank'):
                    Player.objects.filter(nickname=player.nickname).update(tank_rank=player_ranks[rank])
                if (rank == 'damage'):
                    Player.objects.filter(nickname=player.nickname).update(damage_rank=player_ranks[rank])
                if (rank == 'support'):
                    Player.objects.filter(nickname=player.nickname).update(support_rank=player_ranks[rank])
                    