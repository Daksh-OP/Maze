# Invisible Maze

**Invisible Maze** is a "crazy" terminal game where you navigate a hidden maze—blind! The only feedback you get is a snarky insult whenever you bump into a wall. Find the exit at the bottom right corner... if you can.

## How to Play

- **Controls:**  
  Use `W` (up), `A` (left), `S` (down), `D` (right) keys to move.

- **Goal:**  
  Start from the top left (1,1) and reach the exit at the bottom right ([MAZE_SIZE-2, MAZE_SIZE-2]).  
  The maze is invisible; you only know you've hit a wall when the program insults you.

- **Winning:**  
  If you find the exit, you win (and the game will actually be nice for once).

## Game Features

- Randomly generated mazes each play
- Hilariously rude feedback for every wrong move
- No map, no hints—just your memory and grit

## Example Gameplay

```
You are lost in an invisible maze. Try to find the exit!

Use W/A/S/D to move. You only know when you hit a wall. Good luck!

Move (W/A/S/D): D
Move (W/A/S/D): D
Ouch! Did you forget how to walk?
Move (W/A/S/D): S
...
Congratulations! You found the exit. Maybe you aren't hopeless after all.
```

## Installation & Running

1. **Clone this repository:**
   ```sh
   git clone https://github.com/YOUR-USERNAME/invisible-maze.git
   cd invisible-maze
   ```

2. **Run the game:**
   ```sh
   python invisible_maze.py
   ```

   *(Requires Python 3)*

## Customization

- To make the maze bigger or smaller, change the `MAZE_SIZE` variable at the top of `invisible_maze.py`.
- Add your own insults by modifying the `INSULTS` list.

## Tips & Strategy

- Draw a map as you go for best results.
- Systematically try every direction from each new space.
- The exit is always at the bottom right ([MAZE_SIZE-2, MAZE_SIZE-2]).

## License

MIT License

---

Have fun getting roasted by your own code!
