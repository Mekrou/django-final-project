from django import template

register = template.Library()

@register.inclusion_tag('ow2_rank_tracker/rank_display.html')
def display_role(role_name, rank_tier):
    role = role_name.lower()
    
    rank_name, rank_value = separate_division_from_tier(rank_tier)

    role_icon = f"rank_tracker/images/{role}_role_icon.png"
    rank_image = f"/static/rank_tracker/images/{rank_name}.png"
    return {
        'role_name': role_name,
        'role_icon': role_icon,
        'rank_image': rank_image,
        'rank_name': rank_name,
        'rank_value': rank_value,
    }

# Needed because ranks are stored with division and tier
# (master1) when we need (master) for image path
# In hindsight, i should have stored division and tier separately in the model
def separate_division_from_tier(input_string):
    letters = []
    numbers = []

    for char in input_string:
        if char.isalpha():
            letters.append(char)
        elif char.isdigit():
            numbers.append(char)
            break
    if (len(numbers) > 0):
        return ''.join(letters), numbers[0]
    else:
        return ''.join(letters), ''