import requests
from .models import Player

api_base_url = "https://overfast-api.tekrop.fr/"

# returns players rank in Players db model format for each role
# EX: "grandmaster1", "bronze2", etc.
def get_player_ranks(battlenet_id : str):
    try:
        response = requests.get(api_base_url + 'players/' + battlenet_id)
        if response.status_code == 200:
            data = response.json()
            # This is mainly used for logging
            nickname = data['summary']['username']

            # Check if user profile is private
            if (data['summary']['privacy'] == 'private'):
                update_db_if_profile_private(data)
                return None

            # We'll store ranks in here
            ranks = {'tank' : None, 'damage': None, 'support': None}
            ranks_data = data['summary']['competitive']['pc']
            for role in ranks:
                try:
                    ranks[role] = ranks_data[role]['division'] + (str) (ranks_data[role]['tier'])
                except TypeError as e:
                    print(f"{nickname} did not play {role} last season.")
                    ranks[role] = 'unranked'
            return ranks
        else:
            print(f"{battlenet_id} was {response.reason}")
    except requests.RequestException as e:
        print(f"Request error: {e}")
        return None

def update_db_if_profile_private(data):
    nickname = data['summary']['username']
    print(f"{nickname} profile private. Cannot retrieve rank data!")
    print(" Setting ranks to unknown in db..")
    Player.objects.filter(nickname=nickname).update(tank_rank="unknown")
    Player.objects.filter(nickname=nickname).update(damage_rank="unknown")
    Player.objects.filter(nickname=nickname).update(support_rank="unknown")

def populate_db_with_player_ranks():
    players = Player.objects.all()
    for player in players:
        battlenet_id = player.nickname + "-" + player.player_id
        
        player_ranks = get_player_ranks(battlenet_id)
        if (player_ranks):
            for rank in player_ranks:
                if (rank == 'tank'):
                    Player.objects.filter(nickname=player.nickname).update(tank_rank=player_ranks[rank])
                if (rank == 'damage'):
                    Player.objects.filter(nickname=player.nickname).update(damage_rank=player_ranks[rank])
                if (rank == 'support'):
                    Player.objects.filter(nickname=player.nickname).update(support_rank=player_ranks[rank])

def update_player_ranks(battlenet_id):
    battlenet_id = battlenet_id.replace('#', '-')
    nickname, battlenet_number = battlenet_id.split('-')
    player_ranks = get_player_ranks(battlenet_id)
    print(f"found ranks: {player_ranks}")
    if (player_ranks):
        for rank in player_ranks:
            if (rank == 'tank'):
                Player.objects.filter(player_id=battlenet_number).update(tank_rank=player_ranks[rank])
            if (rank == 'damage'):
                Player.objects.filter(player_id=battlenet_number).update(damage_rank=player_ranks[rank])
            if (rank == 'support'):
                Player.objects.filter(player_id=battlenet_number).update(support_rank=player_ranks[rank])