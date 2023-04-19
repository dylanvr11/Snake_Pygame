
# Snake Pygame

This is a simple implementation of the classic Snake Game using Pygame. The game includes a main menu and an options screen.

## Requeriments
- Python 3
- Pygame

## How to play
- Clone this repository.
- Install the requirements

```bash
  pip install -r requiremets.txt
```
- Run python main.py to start the game.
- Use the arrow keys to move the snake.
- Eat the food to increase your score.
- Don't run into the walls or your own body!
- Use the main menu to start a new game, change options or quit.
## Documentation

This code implements a simple Snake game using the Pygame module in Python. The game consists of a snake that moves around the screen and must eat food to increase its size and score. If the snake collides with the screen borders or itself, the game ends.

The code uses the following libraries:

- pygame: a library for creating games in Python.
- sys: a library that provides access to some variables used or maintained by the interpreter and functions that interact with the interpreter.
- time: a library that provides various functions related to time.
- random: a library that provides functions for generating random numbers.

The code uses the following functions:

- The food() function generates a new random position for the food on the screen.

- The snake() function implements the game itself. It starts by initializing some variables, such as the position and size of the snake, the initial direction, the food, and the score. Then, it enters a main loop where it handles keyboard events and updates the position of the snake based on the direction. It also handles collision with the food and updates the score and the position of the food if necessary. Finally, it draws the snake and the food on the screen, displays the score, and checks if the snake collides with the screen borders or itself to determine if the game has ended.

- The get_font() function returns a custom font in the desired size.

- The options() function implements the options screen. It is very simple and only displays a text message and a button to return to the main menu.

- The main_menu() function implements the main menu screen. It displays three buttons: one to play, one to access the options, and one to quit the game. It also handles mouse events and calls the corresponding functions according to the pressed button. If the play button is pressed, the game starts. If the options button is pressed, the options screen is displayed. If the quit button is pressed, the game ends.
