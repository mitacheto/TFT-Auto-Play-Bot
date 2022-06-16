class Champion:
    name = None
    amount = None
    imp_path = None

    def __init__(self, name, amount, img_path):
        self.name = name
        self.amount = amount
        self.imp_path = img_path

    def champ_bought(self):
        self.amount = self.amount - 1

champs = [
    {
        "name": "Ezreal",
        "amount": 3,
        "img_path": "champs_cards/Ezreal.png"
    },
    {
        "name": "Varus",
        "amount": 9,
        "img_path": "champs_cards/Varus.png"
    },
    {
        "name": "Karma",
        "amount": 9,
        "img_path": "champs_cards/Karma.png"
    },
]

def generate_champs():
    generated = []
    for champ in champs:
        generated.append(Champion(champ["name"], champ["amount"], champ["img_path"]))
    return generated