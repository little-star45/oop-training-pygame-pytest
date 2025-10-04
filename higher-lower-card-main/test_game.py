from main import Game
#pytest

class FakeCard:
    def __init__(self, value):
        self.value = value

def test_wrong_guess_loses_points():
    #start new game
    game = Game()
    game.start()

    # ----mock - sztuczne wstawienie danych - nie potrzebuję pełnej klasy Card tylko samego obiektu który ma atrybut .value
    # type() -> tutaj tworzy klasę dynamicznie i od razu nadaje atrybut .value=10

    #manually set the active card and the next card so that the player makes a mistake
    #ręcznie ustawiamy warunki, nie bierzemy z puli bo tam za każdym razem wylosujemy inną kartę;
    game.active_card = type(
        "FakeCard", #nazwa klasy
        (), # Bazy (dziedziczenie) - tutaj brak
        {"value": 10} #Słownik atrybutów i metod
        )
    game.deck.hand_cards.append(type("FakeCard", (), {"value": 5})()) # the player will make a mistake because 5 < 10, and will choose 'h'
    
    #symulujemy, wybór gracza - gracz zakłąda, że kolejna karta będzie wyższa
    _, _, result = game.play_turn('h')

    assert result is False # bo 5 < 10, więc gracz się pomylił
    assert game.score == 35

def test_right_guess_added_points():
    #start new game
    game = Game()
    game.start()

    #inny sposób na definiowanie karty
    game.active_card = FakeCard(10)
    game.deck.hand_cards.append(FakeCard(5))

    _, _, result = game.play_turn('l')

    assert result is True
    assert game.score == 70

def test_no_cards_left_returns_none():
    game=Game()
    game.start()

    game.deck.hand_cards = [] # ręcznie opróżniamy talię gracza
    game.active_card = FakeCard(10) # w sumie nie trzeba ale dla zasady, zeby nie było losowości

    next_card, score_change, result = game.play_turn('h')

    assert next_card is None
    assert score_change is None
    assert result is False

def test_check_score():
    "Test: sprawdzenie czy check_score() działa poprawnie"
    game = Game()
    game.start()

    assert game.check_score() is 50
    game.score = 60
    assert game.check_score() is 60

def test_reset_score():
    game = Game()
    game.start()

    # game.change_score(25) - bo mógłby być tutaj błąd i wtedy go nie wyłapiemy
    game.score = 75 #ustawiam ręcznie dla większej precyzyjności
    assert game.check_score() == 75

    game.reset_score()
    assert game.check_score() == 50 
