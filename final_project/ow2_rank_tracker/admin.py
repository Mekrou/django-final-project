from django.contrib import admin
from .models import Player

class PlayerAdmin(admin.ModelAdmin):
    list_display = ["nickname", "player_id", "tank_rank", "damage_rank", "support_rank"]
    

admin.site.register(Player, PlayerAdmin)