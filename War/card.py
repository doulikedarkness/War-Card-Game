"""
Base class that contains card paramathers and values
"""

#values [ rank : power ]

values = {
    'Dweller':1,
    'Farmer':2,
    'Engineer':3,
    'Miner':4,
    'Blacksmith':5,
    'Alchemist':6,
    'Fighter':7,
    'Knight':8,
    'Priest':9,
    'Lord':10,
    'King':11,
    'Queen':12,
    'Creator':13
}

#clans

clans = ('Dark Ages', 'Edo Shogunate', 'Kahuna Papyrus', 'Hide n seek')

#ranks

ranks = ('Dweller', 'Farmer', 'Engineer', 'Miner', 'Blacksmith', 'Alchemist', 'Fighter', 'Knight', 'Priest', 'Lord', 'King', 'Queen', 'Creator')

#names

random_names = ('Shantae', 'Kirigaya', 'Albedo', 'Lyhoman', 'Star', 'Shrimp', 'Shfart', 'Joji', 'Gura', 'Ame', 'Ken', 'Kuro', 'Shiro', 'Shinji', 'Paimon', 'Tharja', 'Darling', 'Arararagi', 'Rickrolled', 'Toradora', 'Big tiddie gf', 'Smol tiddie goth gf', 'Ricardo', 'Spongebob', 'Bo Burnham', 'Monika', 'Padowu Padowu', 'Scooby-Doo', 'AppleJack', 'Based', 'Bahh Tee', 'Sportacus', 'Asuka')

class Card():

    def __init__(self, card_name, card_clan, card_rank):
        self.card_name = card_name
        self.card_clan = card_clan
        self.card_rank = card_rank
        self.card_value = values[card_rank]

    def __str__(self):
        return f'Card {self.card_name}, which is a part of {self.card_clan} clan and has a rank of {self.card_rank}'
