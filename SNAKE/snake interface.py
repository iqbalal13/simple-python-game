import random
import curses

# Initialize the screen
stdscr = curses.initscr()
curses.curs_set(0)
sh, sw = stdscr.getmaxyx()
w = curses.newwin(sh, sw, 0, 0)
w.keypad(1)
w.timeout(100)

# Create the snake
snake_x = sw//4
snake_y = sh//2
snake = [
    [snake_y, snake_x],
    [snake_y, snake_x-1],
    [snake_y, snake_x-2]
]

# Create the food
food = [sh//2, sw//2]
w.addch(int(food[0]), int(food[1]), curses.ACS_PI)

# Initialize the game variables
key = curses.KEY_RIGHT
score = 0

# Game logic
while True:
    next_key = w.getch()
    key = key if next_key == -1 else next_key

    # Calculate the new head of the snake
    new_head = [snake[0][0], snake[0][1]]

    # Determine movement direction based on the key
    if key == curses.KEY_DOWN:
        new_head[0] += 1
    if key == curses.KEY_UP:
        new_head[0] -= 1
    if key == curses.KEY_LEFT:
        new_head[1] -= 1
    if key == curses.KEY_RIGHT:
        new_head[1] += 1

    # Insert new head at the beginning of the snake
    snake.insert(0, new_head)

    # Check if the snake has hit the wall or itself
    if (
        snake[0][0] in [0, sh] or
        snake[0][1] in [0, sw] or
        snake[0] in snake[1:]
    ):
        curses.endwin()
        quit()

    # Check if snake has eaten the food
    if snake[0] == food:
        score += 1
        food = None
        while food is None:
            nf = [
                random.randint(1, sh-1),
                random.randint(1, sw-1)
            ]
            food = nf if nf not in snake else None
        w.addch(food[0], food[1], curses.ACS_PI)
    else:
        # Move snake
        tail = snake.pop()
        w.addch(int(tail[0]), int(tail[1]), ' ')

    # Display snake
    w.addch(int(snake[0][0]), int(snake[0][1]), curses.ACS_CKBOARD)

    # Display score
    w.addstr(0, 2, 'Score: ' + str(score))

    # Refresh the screen
    w.refresh()