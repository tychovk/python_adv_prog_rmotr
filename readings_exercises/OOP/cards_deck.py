import random

class Card:
    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 
                  'Jack', 'Queen', 'King']
    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank
        
    def __str__(self):
        return "{} of {}".format(Card.rank_names[self.rank],
                Card.suit_names[self.suit])
                
    def compare(self, other):
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        if t1[0] > t2[0]:
            return True
        elif t1[0] == t2[0]:
            if t1[1] > t2[1]:
                return True
            elif t1[1] < t2[1]:
                return False
        elif t1[0] < t2[0]:
            return False
        else:
            return None
        
        
class Deck:
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1,14):
                card = Card(suit, rank)
                self.cards.append(card)
    
    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)
        
    def draw_card(self):
        return self.cards.pop()
        
    def shuffle(self):
        random.shuffle(self.cards)
        
    def add_card(self, card):
        self.cards.append(card)
        
    def move_card(self, hand, num):
        for i in range(num):
            hand.add_card(self.draw_card())
            
    def deal_hands(self, num_hands, cards_hands):
        dealt_hands = []
        for x in range(num_hands):
            hand = Hand()
            self.move_card(hand, cards_hands)
            dealt_hands.append(hand)
            
        return dealt_hands
        
class Hand(Deck):
    """Represents a hand of playing cards."""
    def __init__(self, label=''):
        self.cards = []
        self.label = label
    
            
deck = Deck()
deck.shuffle()

hand1 = Hand('Hand player 1')
deck.move_card(hand1, 7)

print (hand1)

hand2 = Hand('Hand player 2')
deck.move_card(hand2, 7)

print ('\n\n', hand2)

dealt_hands = deck.deal_hands(3, 7)


print (dealt_hands)