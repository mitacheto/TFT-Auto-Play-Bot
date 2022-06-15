from vision import Vision


def getChampImage(champ_name):
    return 'champs_cards\{}.png'.format(champ_name)

def generateComp():

    created_comp_array = []

    comp_array = [
        {
            "name": "Ezreal",
            "level": "3"
        },
        {
            "name": "Karma",
            "level": "3"
        },
        {
            "name": "Leona",
            "level": "3"
        },
        {
            "name": "Taric",
            "level": "3"
        },
        {
            "name": "Ashe",
            "level": "3"
        },
        {
            "name": "LeeSin",
            "level": "3"
        },
        {
            "name": "ShiOhYu",
            "level": "3"
        }
    ]

    for champs in comp_array:
        created_comp_array.append(Vision(getChampImage(champs['name'])))

    return created_comp_array