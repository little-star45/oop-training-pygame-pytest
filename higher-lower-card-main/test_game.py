from main import Game, Deck, Card
from pytest import raises

# pytest

#------BASIC TESTS------

class FakeCard:
    def __init__(self, value):
        self.value = value

def test_wrong_guess_loses_points():
    # Unit test
    # Start a new game
    game = Game()
    game.start()

    # Mock – we don’t need a full Card class, only an object with .value
    # type() -> dynamically creates a class and assigns .value = 10

    # Manually set the active card and the next card so that the player makes a wrong guess
    game.active_card = type(
        "FakeCard",  # class name
        (),          # bases – here: none
        {"value": 10}  # attributes/methods
    )
    game.deck.hand_cards.append(type("FakeCard", (), {"value": 5})())  # player will make a mistake because 5 < 10, but chooses 'h'
    
    # Simulate the player's choice – assumes next card will be higher
    _, _, result = game.play_turn('h')

    assert result is False  # because 5 < 10, so the player was wrong
    assert game.score == 35

def test_right_guess_added_points():
    # Unit test
    game = Game()
    game.start()

    # Another way of defining a card
    game.active_card = FakeCard(10)
    game.deck.hand_cards.append(FakeCard(5))

    _, _, result = game.play_turn('l')

    assert result is True
    assert game.score == 70

def test_no_cards_left_returns_none():
    # Unit test
    game = Game()
    game.start()

    game.deck.hand_cards = []  # manually empty player's hand
    game.active_card = FakeCard(10)  # not necessary, but keeps things predictable

    next_card, score_change, result = game.play_turn('h')

    assert next_card is None
    assert score_change is None
    assert result is False

def test_check_score():
    # Unit test
    # Test: check if check_score() works correctly
    game = Game()
    game.start()

    assert game.check_score() == 50
    game.score = 60
    assert game.check_score() == 60

def test_reset_score():
    # Unit test
    game = Game()
    game.start()

    # Avoid change_score() in case it's buggy – we test reset here only
    game.score = 75  # set manually for precision
    assert game.check_score() == 75

    game.reset_score()
    assert game.check_score() == 50 

def test_has_more_cards_on_hand():
    # Unit test
    # Test: check if has_more_cards_on_hand() works properly
    game = Game()
    game.start()

    assert game.has_more_cards_on_hand() == True

    game.deck.hand_cards = []
    assert game.has_more_cards_on_hand() == False

def test_hand_cards_after_start():
    # Integration test
    # Test: number of cards in hand after starting the game
    # We check isinstance for the first time here, because here we care about the type of active_card
    game = Game()
    game.start()

    # One card goes to active_card, rest stays in hand
    assert game.deck.hand_size == game.NCARDS - 1
    assert isinstance(game.active_card, Card)

def test_grab_hand_takes_cards_from_deck():
    # Unit test
    # Test: grab_hand actually removes cards from deck
    deck = Deck()
    original_deck_size = len(deck.cards)

    hand = deck.grab_hand(8)

    assert len(hand) == 8
    assert len(deck.cards) == original_deck_size - 8

def test_get_card_returns_none_if_empty():
    # Unit test
    # Test: get_card() returns None if no cards left
    deck = Deck()
    deck.hand_cards = []

    assert deck.get_card() == None

def test_play_turn_wrong_letter():
    # Unit test
    # Test: check that method handles invalid input like 'x'
    game = Game()
    
    with raises(ValueError) as excinfo:
        game.play_turn('x')
    
    assert "Invalid answer" in str(excinfo.value)

def test_shuffle_preserves_cards_but_changes_order():
    # Integration test
    deck = Deck()
    original = deck.cards.copy()

    deck.shuffle()
    shuffled = deck.cards

    # Same elements (same content)
    assert sorted(original, key=lambda c: (c.suit, c.rank)) == sorted(shuffled, key=lambda c: (c.suit, c.rank))

    # Different order (most likely)
    assert original != shuffled
