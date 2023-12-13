from django import template
import random
from ow2_rank_tracker import overfast_api

register = template.Library()

@register.inclusion_tag('map_picker/map_template.html')
def display_map(gamemode_picked):
    key = overfast_api.get_gamemode_key(gamemode_picked)
    maps = overfast_api.filter_maps_from_gamemode(key)
    picked_map = random.choice(maps)

    return {
        'map_name': picked_map.name,
        'map_image': picked_map.image,
    }