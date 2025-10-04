# Higher or Lower — Card Game

## Game Description

"**Higher or Lower**" is a simple card game where the player guesses whether the next card drawn from the deck will have a higher or lower value than the current active card. The player earns points for correct guesses and loses points for incorrect ones. The game continues until the player runs out of cards in hand.

### Rules

- The player is dealt 8 cards at the start.
- One card is revealed as the `active_card`.
- The player guesses if the next card will be higher (`h`) or lower (`l`).
- Correct guess: +20 points.
- Wrong guess: -15 points.
- The game ends when no more cards remain in the player's hand.

## Technologies Used

- **Python 3** — main programming language.
- **`random` module** — used for shuffling the deck.
- **pytest** — testing framework for unit and integration tests.
- **Object-Oriented Programming (OOP)** — the game logic is implemented using three classes: `Card`, `Deck`, and `Game`.
- **Unit testing** with mocks (e.g., `FakeCard`) to isolate tests.

## Project Structure

- `main.py` — contains the class-based implementation of the game.
- `test_main.py` — contains unit and integration tests written using `pytest`.
