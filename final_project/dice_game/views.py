from django.shortcuts import render

# Create your views here.

def dice_game(request):
    return render(request, 'dice_game/game.html')
