import requests

api_base_url = "https://overfast-api.tekrop.fr/"

# returns players rank in Players db model format for each role
# EX: "grandmaster1", "bronze2", etc.
def get_player_ranks(player_id):
    # player_id is Name-Id format
    # we should only have to supply this function either ID or Name, and via our db
    # it should be able to find it.
    try:
        response = requests.get(api_base_url + 'players/' + player_id + '/')
        if response.status_code == 200:
            ranks = {'tank' : None, 'damage': None, 'support': None}
            data = response.json()
            ranks_data = data['summary']['competitive']['pc']
            for role in ranks:
                ranks[role] = ranks_data[role]['division'] + (str) (ranks_data[role]['tier'])
            return ranks
    except requests.RequestException as e:
        print(f"Request error: {e}")
        return None