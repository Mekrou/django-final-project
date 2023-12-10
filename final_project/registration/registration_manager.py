from ow2_rank_tracker.models import Player

def contains_symbols(input_string):
    # Check if the string contains symbols
    for char in input_string:
        if not char.isalnum() and not char.isspace():
            return True
    return False

def is_valid_battlenet(input):
    # Does the input have an id? (There is a # in it?)
    result = input.split('#')

    # len(result) should always be 2
    if not (len(result) == 2):
        # Then we know that there was no '#' found in the input
        return False
    # If there is, lets get the username and id number
    # id's are randomly generated, so I have no parameters
    # to validate off of, so it is never used.
    username, id = input.split('#')
    
    # The username must be between 3-12 characters long.
    length = len(username)
    if (length < 3 or length > 12):
        return False
    
    # Usernames cannot start with a number
    if username[0].isdigit():
        return False
    
    # Usernames cannot contain symbols (including spaces)
    if contains_symbols(username):
        return False
    
    # If we passed all checks, it's valid!
    return True

def is_battlenet_in_database(input):
    username, id = input.split('#')

    try:
        # search for our player
        player_object = Player.objects.filter(nickname=username, player_id=id)

        # attempting to access player's nickname
        # will throw an error if it was not found
        # which is what we want.
        player_object.first().nickname

        # no error means it is in DB
        return True
    except (AttributeError) as e:
        #print(f"{input} was not found in the database!")
        return False