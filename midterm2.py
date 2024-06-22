import random

def generate_path(N, M):
    # Create a 2D list of zeros representing the maze map
    maze = [[0 for _ in range(M)] for _ in range(N)]
    path = [(0, 0)]

    # Start at the top-left cell and add it to the path
    x, y = 0, 0
    maze[x][y] = 2  # Mark as part of the path

    # Generate a path to the bottom-right cell
    while (x, y) != (N-1, M-1):
        if x == N-1:
            y += 1  # Move right
        elif y == M-1:
            x += 1  # Move down
        else:
            if random.choice([True, False]):
                y += 1  # Move right
            else:
                x += 1  # Move down
        maze[x][y] = 2  # Mark as part of the path
        path.append((x, y))

    return maze, path

def add_obstacles(maze, path, num_obstacles):
    N = len(maze)
    M = len(maze[0])
    obstacles = 0

    while obstacles < num_obstacles:
        x = random.randint(0, N-1)
        y = random.randint(0, M-1)

        if (x, y) not in path and maze[x][y] != 1:
            maze[x][y] = 1  # Mark as an obstacle
            obstacles += 1

    return maze

def generate_maze(N, M, num_obstacles):
    maze, path = generate_path(N, M)
    maze = add_obstacles(maze, path, num_obstacles)
    return maze

def print_maze(maze):
    # Print the maze map as a grid
    print("+" + "---+" * len(maze[0]))
    for row in maze:
        row_str = "|"
        for cell in row:
            if cell == 0:
                row_str += "   "
            elif cell == 1:
                row_str += " X "
            elif cell == 2:
                row_str += "   "
            row_str += "|"
        print(row_str)
        print("+" + "---+" * len(maze[0]))

# Prompt the user to input the values of N, M, and num_obstacles
N = int(input("Enter the number of rows (N): "))
M = int(input("Enter the number of columns (M): "))
max_possible_obs = N * M - (N + M - 1)
num_obstacles = int(input(f"Enter the number of obstacles (0-{max_possible_obs}): "))
while num_obstacles < 0 or num_obstacles > max_possible_obs:
    num_obstacles = int(input(f"Re-enter the number of obstacles (0-{max_possible_obs}): "))

# Generate the maze using the user-specified values
maze = generate_maze(N, M, num_obstacles)

# Print the generated maze as a grid to the console
print("Generated Maze Map:")
print_maze(maze)
