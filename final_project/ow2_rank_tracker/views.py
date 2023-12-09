from django.shortcuts import render
from .overfast_api import get_player_ranks
from .models import Player

players = Player.objects.all()

# Create your views here.
def index(request):
    return render(request, 'ow2_rank_tracker/index.html')


def populate_db_with_player_ranks():
    for player in players:
        player.rank = get_player_ranks(player.player_id)