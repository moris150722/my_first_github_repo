import random

def generate_path(maze, N, M):
    path = [(0, 0)]
    maze[(0, 0)] = 2

    i, j = 0, 0
    while i < N - 1 or j < M - 1:
        if i == N - 1:
            j += 1
        elif j == M - 1:
            i += 1
        else:
            if random.choice([True, False]):
                i += 1
            else:
                j += 1
        path.append((i, j))
        maze[(i, j)] = 2

    return maze

def add_obstacles(maze, min_obstacles, N, M):
    empty_cells = [(i, j) for i in range(N) for j in range(M) if maze[(i, j)] == 0]
    for _ in range(min_obstacles):
        if not empty_cells:
            break
        cell = random.choice(empty_cells)
        maze[cell] = 1
        empty_cells.remove(cell)
    return maze

def set_obstacle(maze, N, M):
    while True:
        try:
            x, y = map(int, input("Enter the coordinates to set an obstacle (x,y): ").split(","))
            if (x, y) in maze and maze[(x, y)] != 2:
                maze[(x, y)] = 1
                break
            else:
                print("Cannot set obstacle on the path or outside the grid.")
        except (ValueError, KeyError):
            print("ValueError in set_obstacle function. Need to be coordinates.")

    return maze

def remove_obstacle(maze, N, M):
    while True:
        try:
            x, y = map(int, input("Enter the coordinates to remove an obstacle (x,y): ").split(","))
            if (x, y) in maze and maze[(x, y)] == 1:
                maze[(x, y)] = 0
                break
            else:
                print("No obstacle found at the given coordinates or it's part of the path.")
        except (ValueError, KeyError):
            print("ValueError in remove_obstacle function. Need to be coordinates.")

    return maze

def print_maze(maze, N, M):
    for i in range(N):
        print("+---" * M + "+")
        for j in range(M):
            if maze[(i, j)] == 0:
                print("|   ", end="")
            elif maze[(i, j)] == 1:
                print("| X ", end="")
            elif maze[(i, j)] == 2:
                print("| O ", end="")
        print("|")
    print("+---" * M + "+")

def print_file_contents(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            for line in lines:
                print(line.strip())
    except IOError:
        print("Error: File not found. Please enter a valid file name.")

def main():
    while True:
        filename = input("Enter the maze file name (e.g., grid77.txt or grid99.txt): ")
        print_file_contents(filename)
        
        try:
            with open(filename, 'r') as file:
                lines = file.readlines()
                N = (len(lines) - 1) // 2
                M = (len(lines[0].strip()) - 1) // 4
                maze = {}
                for i in range(N):
                    for j in range(M):
                        maze[(i, j)] = 0 if lines[2 * i + 1][4 * j + 2] == ' ' else 1
        except IOError:
            print("Error: File not found. Please enter a valid file name.")
            continue
        except IndexError:
            print("Invalid file format. Please check the file contents.")
            continue

        break

    while True:
        try:
            min_obstacles = int(input("Enter the minimum number of obstacles to add: "))
            if min_obstacles < 0 or min_obstacles >= N * M:
                raise ValueError
            break
        except ValueError:
            print("Invalid number. Please enter a valid number.")

    maze = generate_path(maze, N, M)
    maze = add_obstacles(maze, min_obstacles, N, M)
    print_maze(maze, N, M)

    while True:
        print("\nMenu:\n1. Set obstacle\n2. Remove obstacle\n3. Exit")
        choice = input("Enter your option: ")
        if choice == "1":
            maze = set_obstacle(maze, N, M)
            print_maze(maze, N, M)
        elif choice == "2":
            maze = remove_obstacle(maze, N, M)
            print_maze(maze, N, M)
      
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

    print("Goodbye!")

if __name__ == "__main__":
    main()
