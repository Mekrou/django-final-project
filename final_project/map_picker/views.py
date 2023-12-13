from django.shortcuts import render
from ow2_rank_tracker import overfast_api


# Create your views here.
def map_picker(request):
    gamemodes = overfast_api.get_gamemode_names()
    
    selected_gamemode = request.POST.get('selected_gamemode')
    if (selected_gamemode):
        return render(request, 'map_picker/map_picker.html', {'gamemodes' : gamemodes, "gamemode_picked" : selected_gamemode})
        NotImplementedError

    return render(request, 'map_picker/map_picker.html', {'gamemodes' : gamemodes})