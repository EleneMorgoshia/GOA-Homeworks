 #GET PLANET NAME BY ID

def get_planet_name(id):
    name = ""
    match id:
        case 1 :
            name += 'Mercury'
        case 2 :
            name += 'Venera'
        case 3 :
            name += 'Earth'
        case 4 :
            name += 'Mars'
        case 5 :
            name += 'jupiter'
        case 7 :
            name += 'Saturn'
        case 8:
            name += 'Neptune'
    return name 

print(get_planet_name(1))