from random import choice

class TarotDeck:
    
    def create_suit(self, suit):
        cards = []
        cards.append(f"Ace of {suit}")
        cards += map(lambda n: f"{n} {suit}", range(2,11))
        cards += map(lambda n: f"{n} of {suit}", ['Page', 'Knight', 'Queen', 'King'])
        return cards
        
    def __init__(self):
        self.cards = ['The Fool', 'The Magician', 'The High Priestess', 'The Empress', 'The Emperor', 'The Hierophant', 'The Lovers', 'The Chariot', 'Strength', 'The Hermit', 'Wheel of Fortune', 'Justice', 'The Hanged Man', 'Death', 'Temperance', 'The Devil', 'The Tower', 'The Star', 'The Moon', 'The Sun', 'Judgement', 'The World']
        
        self.cards += sum(map(self.create_suit, ['Wands', 'Cups', 'Swords', 'Pentacles']), []) # flatten the nested arrays


    def random_card(self):
        return choice(self.cards)

