import random

def computer_choice(arr):
    """Randomly choose an available position, retrying recursively if occupied.

    :param arr: The board containing at least one available integer position.
    :return: The chosen available position as an integer.
    """
    choice = random.choice(random.choice(arr))
    if isinstance(choice, int):
        return choice
    else: #recursion
        return computer_choice(arr)

def create_arr(rows, cols):
    """Create a board with positions numbered consecutively from one.

    :param rows: The number of rows to create.
    :param cols: The number of columns to create.
    :return: A nested list containing the numbered board positions.
    """
    # [[1,2,3],
    #  [4,5,6],
    #  [7,8,9]]
    count = 1
    arr = []
    for i in range(rows):
        arr.append([])
        for j in range(1, cols + 1):
            arr[i].append(count)
            count += 1
    return arr

def find_number(arr, num, choice):
    """Replace a numbered position with a player's symbol in place.

    :param arr: The board to update.
    :param num: The numbered position to replace.
    :param choice: The symbol to place, either "X" or "O".
    :return: The same board list, updated if the position was found.
    """
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == num:
                arr[i][j] = choice
    return arr


def create_board(arr):
    """Print the board with aligned cells and borders.

    :param arr: A nonempty rectangular board of numbered positions and symbols.
    :return: None.
    """
    width = len(str(len(arr) * len(arr[0])))
    border = "-" * (width + 2)

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            value = str(arr[i][j]).rjust(width)
            print(f" {value} ", end="")

            if j < len(arr[i]) - 1:
                print("|", end="")
        print()

        if i < len(arr) - 1:
            print((border + "+") * (len(arr[i]) - 1) + border)

def cross_circle():
    """Ask for cross or circle until the player enters a valid choice.

    :return: A tuple containing the user's symbol and the computer's symbol.
    """
    while True:
        choice = input("Enter cross or circle: ").lower().strip()

        if choice == "cross":
            return "X", "O"
        elif choice == "circle":
            return "O", "X"

        print("Please enter cross or circle.")

def int_in_arr(arr):
    """Check whether the board still contains an available integer position.

    :param arr: The board to check for available positions.
    :return: True if an integer position remains, otherwise False.
    """
    for i in arr:
        for j in i:
            if isinstance(j, int):
                return True
    return False

def horizontal_align(arr, symbol, count_match):
    """Check each row for the required number of matching symbols.

    :param arr: The board to check.
    :param symbol: The player's symbol to count.
    :param count_match: The required number of matching symbols in a row.
    :return: (True, row number) for the first matching row, or (False, 0).
             Row numbers start at one.
    """

    for i in range(len(arr)):
        count = 0
        for j in range(len(arr[i])):
            if arr[i][j] == symbol:
                count += 1
        if count == count_match:
            return True, i+1
    return False, 0

def vertical_align(arr, symbol, count_match):
    """Check each column for the required number of matching symbols.

    :param arr: The square board to check.
    :param symbol: The player's symbol to count.
    :param count_match: The required number of matching symbols in a column.
    :return: (True, column number) for the first matching column, or (False, 0).
             Column numbers start at one.
    """
    counts = []
    #fill with 0 for vertical counts
    for i in range(len(arr)):
        counts.append(0)
    #check
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == symbol:
                counts[j] += 1

    #check counts
    for i in range(len(counts)):
        if counts[i] == count_match:
            return True, i+1
    return False, 0

def diagonal_align(arr, symbol, count_match):
    """Check the main and opposite diagonals for matching symbols.

    :param arr: The square board to check.
    :param symbol: The player's symbol to count.
    :param count_match: The required number of matching symbols on a diagonal.
    :return: (True, "main") or (True, "opposite") for a matching diagonal,
             or (False, "") if neither diagonal matches.
    """
    main_diagonal = 0
    opposite_diagonal = 0
    for i in range(len(arr)):
        if arr[i][i] == symbol:
            main_diagonal += 1
        if arr[i][-(i+1)] == symbol:
            opposite_diagonal += 1
        if main_diagonal == count_match:
            return True, "main"
        if opposite_diagonal == count_match:
            return True, "opposite"
    return False, ""

def is_valid_position(arr, position):
    """Check whether a requested position is still available on the board.

    :param arr: The board of numbered positions and player symbols.
    :param position: The integer position requested by the player.
    :return: True if the position is available, otherwise False.
    """
    for row in arr:
        if position in row:
            return True
    return False

def get_position():
    """Ask for a position until the player enters a whole number.

    :return: The entered integer, which still needs availability validation.
    """
    while True:
        try:
            return int(input("Choose a position: "))
        except ValueError:
            print("Please enter a whole number.")

def get_valid_position(arr):
    """Ask until the player chooses an available position.

    :param arr: The current board.
    :return: An available position as an integer.
    """
    while True:
        position = get_position()
        if is_valid_position(arr, position):
            return position
        print("That position is unavailable. Choose another.")


def get_board_size():
    """Ask the player for the number of rows and columns.

    :return: The entered board size as an integer.
    """
    return int(input("Choose how many rows and columns: (3 for 3x3, 4 for 4x4, etc) "))


def show_result(status, user, horizontal_check, vertical_check, diagonal_check):
    """Print the winning alignment details and return the player's score.

    :param status: The winning symbol from the latest move.
    :param user: The user's symbol.
    :param horizontal_check: A tuple containing the row result and row number.
    :param vertical_check: A tuple containing the column result and column number.
    :param diagonal_check: A tuple containing the diagonal result and its name.
    :return: An integer score of 2 for a user win or 0 for a computer win.
    """
    if status == user:
        print("You win!")
        score = 2
    else:
        print("You lost")
        score = 0
    winner = "You" if status == user else "Your opponent"
    if diagonal_check[0]:
        print(f"{winner} completed {diagonal_check[1]} diagonal.")
    if horizontal_check[0]:
        print(f"{winner} completed row {horizontal_check[1]}.")
    if vertical_check[0]:
        print(f"{winner} completed column {vertical_check[1]}.")
    return score


def play(player_name):
    """Run one Tic-Tac-Toe session on a square board chosen by the player.

    :param player_name: The arcade player's name.
    :return: An integer score of 2 for a win, 1 for a draw, or 0 for a loss.
    """
    #cross first, circle second
    print("Welcome to Tic Tac Toe")
    rows_x_cols = get_board_size()
    score = 0
    user, comp = cross_circle()
    arr = create_arr(rows_x_cols, rows_x_cols)
    # X starts first
    status = "X"
    horizontal_check = (False, 0)
    vertical_check = (False, 0)
    diagonal_check = (False, "")

    while int_in_arr(arr) and not horizontal_check[0] and not vertical_check[0] and not diagonal_check[0]:
        create_board(arr)
        if status == user:
            position = get_valid_position(arr)
        else:
            position = computer_choice(arr)
            print(f"Your opponent chose {position}")
        find_number(arr, position, status)
        horizontal_check = horizontal_align(arr, status, rows_x_cols)
        vertical_check = vertical_align(arr, status, rows_x_cols)
        diagonal_check = diagonal_align(arr, status, rows_x_cols)
        if horizontal_check[0] or vertical_check[0] or diagonal_check[0]:
            score = show_result(status, user, horizontal_check, vertical_check, diagonal_check)
            create_board(arr)
            return score
        status = "O" if status == "X" else "X"

    create_board(arr)

    if not horizontal_check[0] and not vertical_check[0] and not diagonal_check[0]:
        print("It's a draw!")
        score =1
    return score






