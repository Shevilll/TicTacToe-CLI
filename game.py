NUM = [1, 2, 3, 4, 5, 6, 7, 8, 9]

board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]


def create_board(board):
    for board_index, i in enumerate(board):
        for k, j in enumerate(i):
            if k != 2:
                print(j, end="|")
            else:
                print(j)
        if board_index != 2:
            print("-" * 5)
    print("#" * 6)


def enter_move(pos: int, player: str):
    if pos in NUM[:3] and not check_pos(board, pos):
        board[2].pop(pos - 1)
        board[2].insert(pos - 1, player)

    if pos in NUM[3:6] and not check_pos(board, pos):
        board[1].pop(pos - 4)
        board[1].insert(pos - 4, player)

    if pos in NUM[6:9] and not check_pos(board, pos):
        board[0].pop(pos - 7)
        board[0].insert(pos - 7, player)


def check_pos(board, pos):
    if pos in NUM[:3] and (board[2][pos - 1] != " "):
        return True
    if pos in NUM[3:6] and (board[1][pos - 4] != " "):
        return True
    if pos in NUM[6:9] and (board[0][pos - 7] != " "):
        return True


def check_winner(board):
    if (
        board[0][0] == board[0][1] == board[0][2] != " "
        or board[1][0] == board[1][1] == board[1][2] != " "
        or board[2][0] == board[2][1] == board[2][2] != " "
        or board[0][0] == board[1][0] == board[2][0] != " "
        or board[0][1] == board[1][1] == board[2][1] != " "
        or board[0][2] == board[1][2] == board[2][2] != " "
        or board[0][0] == board[1][1] == board[2][2] != " "
        or board[0][2] == board[1][1] == board[2][0] != " "
    ):
        return True


def main():
    try:
        while True:
            create_board(board)
            if " " not in board[0] and " " not in board[1] and " " not in board[2]:
                print("TIE!!")
                return None
            playerx = int(input("Enter the position[x]: "))
            while check_pos(board, playerx) or playerx not in NUM:
                print("Position is Invalid!!")
                playerx = int(input("Enter the position[x]: "))
            enter_move(playerx, "x")
            create_board(board)
            if check_winner(board):
                print("X WON!!")
                return None
            if " " not in board[0] and " " not in board[1] and " " not in board[2]:
                print("TIE!!")
                return None
            playero = int(input("Enter the position[o]: "))
            while check_pos(board, playero) or playero not in NUM:
                print("Position is Invalid!!")
                playero = int(input("Enter the position[o]: "))
            enter_move(playero, "o")
            if check_winner(board):
                create_board(board)
                print("O WON!!")
                return None
    except:
        print("Some Error Occurred")


ch = input("Play New Game(y/n): ").lower()
while __name__ == "__main__" and ch == "y":
    main()
    ch = input("Play New Game(y/n): ").lower()
    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
else:
    print("Thankyou!")
