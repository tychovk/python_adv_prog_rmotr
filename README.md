#A gist of what we did this week

# [pyp-c2-a1] Battleship game

Build a battleship game. It has to work in the console. You don’t need any external libraries, you can make it work just using plain python. You’d play against the console. The game will have 2 play modes: attack and defence.

### Defend mode

In this mode you place the ships and receive attacks from the computer; you’ll have to inform if the attack was successful or not.

When the game starts the computer will give you information about the grid (10x10) and tell you what ships you have available. For example:

1 submarine (size 3)
1 Aircraft (size 5)
2 Patrol boats (size 2)
Then you’ll be able to position them in the grid, indicating the first position and if they should be placed horizontally or vertically. Example:

```
Place the submarine on C3 vertically
Place the aircraft on A9 horizontally
```

At this point the computer must do some checks; namely:

* If the ship fits; it’s not out of bounds. For example, placing an Aircraft on the position H9 horizontally would make it go out of bounds
* If two ships collide. For example. Placing the submarine on C3 vertically and the aircraft on B1 horizontally.

After the setup is done (ship positioning) you’ll start receiving random attacks from the computer; 1 at a time. After the computer attacks it’ll ask for an answer from you (either miss, hit or sunk). You’ll inform the computer (seeing the grid on screen). If you cheat, the computer should know.

Of course the computer would never fire two shots at the same position; and would realize when it sunk all the ships.

Extra: Once the computer identifies it has hit a ship the attacks could stop being random and focus on sinking that particular ship it hit.

### Attack mode

In this mode the computer position the ships and you’ll have to sink all of them. The computer will position the ships randomly. After it’s done it’ll start asking for your shots. Once you fire your shot it’ll inform you if you missed, hit or sunk a ship. Once all the ships are sunk the game finishes and it’ll provide statistics about it.


# [pyp-c1-a2] Sorting Algorithms

Implement Bubble Sort ([http://en.wikipedia.org/wiki/Bubble_sort](http://en.wikipedia.org/wiki/Bubble_sort)) and Insertion Sort ([http://en.wikipedia.org/wiki/Insertion_sort](http://en.wikipedia.org/wiki/Insertion_sort)) algorithms.


# [pyp-c1-a1] Fibonacci numbers
([http://en.wikipedia.org/wiki/Fibonacci_number](http://en.wikipedia.org/wiki/Fibonacci_number))

Write a program that generates the nth number in a fibonacci sequence (starting at 0). The program should start and ask two things:

The number that will describe the nth term you want to get
if the function should be recursive or not
The program should count with data validation. It means that the program must inform the user when the number she inserted is invalid.

Extra: If the user passes a --recursive argument, the program should not ask for the function to use and use the recursive function.



# [pyp-c1-a3] Tic-Tac-Toe

Write a simple program to play a game of Tic-Tac-Toe. The game is between two players. The computer starts displaying the board with all the empty spots and asks for the first move. The computer asks each player for her move; the player will inform the coordinates to place her mark with a letter and a number; the letter indicating the column and the number the row. Example: B2 is the center of the board. A1 is the top left corner of the board. C3 is the bottom right corner (furthermost from the A1).

The computer will keep asking both player for their marks until one of them win or there are no more places in the board to position marks.






