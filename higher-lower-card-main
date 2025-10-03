from random import shuffle

class Card:
    def __init__(self, rank, suit, value):
        self.rank = rank
        self.suit = suit
        self.value = value
    
    def __repr__(self):
        return f"Rank:{self.rank}; Suit:{self.suit}; Value:{self.value}"

class Deck:
    def __init__(self):
        self.cards = self._create_deck()
        self.hand_cards = []
        
    def _create_deck(self):
        suits = ("Spades", "Diamonds", "Hearts", "Clubs")
        ranks = {**{str(i): i for i in range(2, 11)},
                 "Jack": 11, "Queen": 12, "King": 13, "As": 1}
        return [Card(rank, suit, value)
                for suit in suits
                for rank, value in ranks.items()]
                
    def shuffle(self):
        shuffle(self.cards)
    
    def show_deck(self):
        for card in self.cards:
            print(card)
            
    def grab_hand(self, cards_nb):
        for _ in range(cards_nb):
            card = self.cards.pop()
            self.hand_cards.append(card)
        return self.hand_cards
    
    def get_card(self):
        if self.hand_cards:
            return self.hand_cards.pop()
        else:
            None
    
    @property
    def hand_size(self):
        return len(self.hand_cards)

class Game:
    def __init__(self):
        self.NCARDS = 8
        self.deck = Deck()
        self.active_card = None
        self.score = 50
    
    def start(self):
        self.deck.shuffle()
        self.deck.grab_hand(self.NCARDS)
        self.active_card = self.deck.get_card()
    
    def change_score(self,value):
        self.score += value
    
    def reset_score(self):
        self.score = 50
        return self.score
    
    def check_score(self):
        return self.score
    
    def play_turn(self, answer):
        next_card = self.deck.get_card()
        if next_card is None:
            return None, None, False 
        if (self.active_card.value < next_card.value and answer == 'h') or (self.active_card.value > next_card.value and answer == 'l'):
            score_change = self.change_score(20)
            result = True
        else:
            score_change = self.change_score(-15)
            result = False

        self.active_card = next_card
        return next_card, score_change, result
    
    def has_more_cards_on_hand(self):
        return self.deck.hand_size>0
        

def main():
    print("Welcome to Higher or Lower!")
    while True:
        game = Game()
        game.start()

        while game.has_more_cards_on_hand():
            print(f"\nCurrent card: {game.active_card}")
            guess = input("Will the next card be higher or lower? (h/l): ").lower()
            while guess not in ('h', 'l'):
                guess = input("Please enter 'h' or 'l': ").lower()

            next_card, _, result = game.play_turn(guess)

            print(f"Next card: {next_card}")
            print("+20 points!" if result else "-15 points!")
            print(f"Current score: {game.score}")

        print(f"Final score: {game.score}\n")
        if input("Press ENTER to play again, or 'q' to quit: ").lower() == 'q':
            break

    print("Thanks for playing!")

if __name__ == "__main__":
    main()
