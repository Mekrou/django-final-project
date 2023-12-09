from django.db import models

class Player(models.Model):
    RANK_CHOICES = [
        ('bronze1', 'Bronze 1'),
        ('bronze2', 'Bronze 2'),
        ('bronze3', 'Bronze 3'),
        ('bronze4', 'Bronze 4'),
        ('bronze5', 'Bronze 5'),
        ('silver1', 'Silver 1'),
        ('silver2', 'Silver 2'),
        ('silver3', 'Silver 3'),
        ('silver4', 'Silver 4'),
        ('silver5', 'Silver 5'),
        ('gold1', 'Gold 1'),
        ('gold2', 'Gold 2'),
        ('gold3', 'Gold 3'),
        ('gold4', 'Gold 4'),
        ('gold5', 'Gold 5'),
        ('platinum1', 'Platinum 1'),
        ('platinum2', 'Platinum 2'),
        ('platinum3', 'Platinum 3'),
        ('platinum4', 'Platinum 4'),
        ('platinum5', 'Platinum 5'),
        ('diamond1', 'Diamond 1'),
        ('diamond2', 'Diamond 2'),
        ('diamond3', 'Diamond 3'),
        ('diamond4', 'Diamond 4'),
        ('diamond5', 'Diamond 5'),
        ('master1', 'Master 1'),
        ('master2', 'Master 2'),
        ('master3', 'Master 3'),
        ('master4', 'Master 4'),
        ('master5', 'Master 5'),
        ('grandmaster1', 'Grandmaster 1'),
        ('grandmaster2', 'Grandmaster 2'),
        ('grandmaster3', 'Grandmaster 3'),
        ('grandmaster4', 'Grandmaster 4'),
        ('grandmaster5', 'Grandmaster 5'),
        ('top500', 'Top 500'),
    ]


    nickname = models.CharField(max_length=30)
    # Player's battlenet extension (#13505)
    player_id = models.CharField(max_length=8, unique=True)
    tank_rank = models.CharField(max_length=16, choices=RANK_CHOICES, default='bronze1')
    damage_rank = models.CharField(max_length=16, choices=RANK_CHOICES, default='bronze1')
    support_rank = models.CharField(max_length=16, choices=RANK_CHOICES, default='bronze1')