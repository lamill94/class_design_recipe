# {{PROBLEM}} Class Design Recipe

## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._

As a game player
I want to create a `character` with a cool `name`
So that other players recognise my character

As a game player
I want to see my characters `health`
So that I know when I might need to drink a health potion

As a game player
I want my character to be able to `pick up` `items (potions/weapons)` that they find in the game
So that they can use them when they need

As a game player
I want to be able to `use my health potion` item
So that my character's health goes back to 100

As a game player
I want to `attack` another character
So that they lose the health points associated with an attack by that weapon

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python

class GamePlayer():

    def __init__(self, name, health):
        # Parameters:
            # name: string
            # health: int
            # items: an empty list
        # Side effects:
            # Sets the name & health propety of the self object
        pass

    def current_health():
        # Returns:
            # An int showing the player's health
        pass

    def pick_up_item(item, value):
        # Parameters:
            # item: string showing whether it's a potion or weapon
            # value: int showing increase in health or attack damage
        # Side effects:
            # Gets added to the items list
        pass

    def increase_health():
        # Side effects:
            # Removes health potion from items list
            # Increases health to 100
        pass

    def attack(weapon, damage):
        # Params:
            # An int showing amount of damage
        # Side effects:
            # Subtract the damage from the health of the player you're attacking 


```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python

# Check if there's an instance of the class

def test_instance_of_class():
    gamePlayer = GamePlayer("Lauren", 100)
    assert isInstance(gamePlayer, class)

# Check if we can see player's health

def test_current_health():
    gamePlayer = GamePlayer("Lauren", 100)
    result = gamePlayer.current_health
    assert result == 100

# Check if we can pick-up item

def test_pick_up_item():
    gamePlayer = GamePlayer("Lauren", 100)
    gamePlayer.pick_up_item("Health Potion", 50)
    result = gamePlayer.items
    assert result = ["Health Potion"]

# Check if we can pick-up multiple items

def test_pick_up_item():
    gamePlayer = GamePlayer("Lauren", 100)
    gamePlayer.pick_up_item("Health Potion", 50)
    gamePlayer.pick_up_item("Sword", 500)
    result = gamePlayer.items
    assert result = ["Health Potion", "Sword]

# Check if we can increase health

def test_increase_health():
    gamePlayer = GamePlayer("Lauren", 50)
    gamePlayer.pick_up_item("Health Potion", 50)
    gamePlayer.increase_health()
    result = gamePlayer.current_health()
    assert result == 100

# Check if increase health doesn't work if no health potion in items

def test_increase_health():
    gamePlayer = GamePlayer("Lauren", 50)
    gamePlayer.increase_health()
    result = gamePlayer.current_health()
    assert result == 50

```

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
