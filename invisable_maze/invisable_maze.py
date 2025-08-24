import random
import os

MAZE_SIZE = 8
INSULTS = [
    "Ouch! Did you forget how to walk?",
    "That's a wall, genius.",
    "Maybe try using your eyes. Oh wait...",
    "Are you lost, or just bad at this?",
    "Nice job! (Not.)",
    "If brains were dynamite, you wouldn't have enough to blow your nose.",
    "You hit the wall harder than my grandma.",
    "Ever considered a career as a wall inspector?",
    "Even a Roomba would do better.",
    "Is that your final answer?"
]

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def create_maze(size):
    maze = [[0 for _ in range(size)] for _ in range(size)]
    # Surround the maze with walls
    for i in range(size):
        maze[0][i] = 1
        maze[size-1][i] = 1
        maze[i][0] = 1
        maze[i][size-1] = 1
    # Random internal walls
    for _ in range(size*size//3):
        x, y = random.randint(1, size-2), random.randint(1, size-2)
        maze[y][x] = 1
    return maze

def print_status():
    print("You are lost in an invisible maze. Try to find the exit!\n")
    print("Use W/A/S/D to move. You only know when you hit a wall. Good luck!\n")

def play_game():
    maze = create_maze(MAZE_SIZE)
    # Entrance and exit
    player_pos = [1,1]
    exit_pos = [MAZE_SIZE-2, MAZE_SIZE-2]
    maze[player_pos[1]][player_pos[0]] = 0
    maze[exit_pos[1]][exit_pos[0]] = 0

    while True:
        clear()
        print_status()
        if player_pos == exit_pos:
            print("Congratulations! You found the exit. Maybe you aren't hopeless after all.")
            break
        move = input("Move (W/A/S/D): ").strip().upper()
        dx, dy = 0, 0
        if move == "W":
            dy = -1
        elif move == "S":
            dy = 1
        elif move == "A":
            dx = -1
        elif move == "D":
            dx = 1
        else:
            print("That's not even a direction. Try again.")
            input("(Press Enter to continue)")
            continue
        new_x = player_pos[0] + dx
        new_y = player_pos[1] + dy
        if maze[new_y][new_x] == 1:
            print(random.choice(INSULTS))
            input("(Press Enter to continue)")
        else:
            player_pos = [new_x, new_y]

if __name__ == "__main__":
    play_game()