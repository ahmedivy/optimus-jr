import sys
import time


def find_char(board, ch):
    for i, row in enumerate(board):
        for j, char in enumerate(row):
            if char == ch:
                return (i, j)
    return None


def find_second_char(board, ch, current):
    for i, row in enumerate(board):
        for j, char in enumerate(row):
            if char == ch and (i, j) != current:
                return (i, j)
    return None


def main():
    if len(sys.argv) < 2:
        print(f"Usage: python {sys.argv[0]} <filename>")
        return

    filename = sys.argv[1]

    with open(filename, "r") as f:
        lines = f.readlines()
        size, *board = lines
        row, col = map(int, size.split())
        board = [list(row.strip()) for row in board]

    directions = ['SOUTH', 'EAST', 'NORTH', 'WEST']

    start = find_char(board, '@')
    current_direction = 0
    breaker_mode = False
    obstacle_flag = False
    direction_flag = False

    path = []

    start_time = time.time()

    while True:

        i, j = start
        direction = directions[current_direction]

        match direction:
            case 'SOUTH':
                i += 1
            case 'EAST':
                j += 1
            case 'NORTH':
                i -= 1
            case 'WEST':
                j -= 1

        match board[i][j]:
            case ' ':
                start = (i, j)
                path.append(direction)
            case '#':
                if not obstacle_flag:
                    current_direction = 0 if not direction_flag else 3
                else:
                    current_direction = (
                        current_direction + 1) % 4 if not direction_flag else (current_direction - 1) % 4
                obstacle_flag = True
            case '$':
                path.append(direction)
                break
            case 'S':
                current_direction = 0
                start = (i, j)
                path.append(direction)
            case 'E':
                current_direction = 1
                start = (i, j)
                path.append(direction)
            case 'N':
                current_direction = 2
                start = (i, j)
                path.append(direction)
            case 'W':
                current_direction = 3
                start = (i, j)
                path.append(direction)
            case 'I':
                direction_flag = not direction_flag
                start = (i, j)
                path.append(direction)
            case 'B':
                breaker_mode = not breaker_mode
                start = (i, j)
                path.append(direction)
            case 'X':
                if breaker_mode:
                    start = (i, j)
                    path.append(direction)
                else:
                    if not obstacle_flag:
                        current_direction = 0 if not direction_flag else 3
                    else:
                        current_direction = (current_direction + 1) % 4 if not direction_flag else (
                            current_direction - 1) % 4
                    obstacle_flag = True
            case '@':
                print("LOOP")
                return
            case _:
                if board[i][j].isnumeric():
                    start = find_second_char(board, board[i][j], (i, j))
                    path.append(direction)

        if time.time() - start_time > 1:
            print("LOOP")
            return

        if board[i][j] != '#' and board[i][j] != 'X':
            obstacle_flag = False

    for direction in path:
        print(direction)


if __name__ == "__main__":
    main()
