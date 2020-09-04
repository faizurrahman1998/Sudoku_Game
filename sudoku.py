def print_board(board):

    for i in range(len(board)):

        if (i % 3 == 0 and i != 0):
            print("-----------------------")

        for j in range(len(board[i])):

            if (j % 3 == 0 and j != 0 ):
                print(" |", end = "")
            
            print(f" {board[i][j]}", end="")
        
        print()


def find_slot(board, row):

    for i in range(row, len(board)):
        for j in range(9):
            try:

                if (board[i][j] == 0):
                    return (True, i, j)
            
            except IndexError:
                print(i, j)
        
    return (False, 0, 0)

def check_validity(board, co_ordinates, number):

    verdicts = [True, True, True]

    #checking the row
    verdicts[0] = (number not in board[co_ordinates[1]])

    for i in range(9):

        if (board[i][co_ordinates[2]] == number):
            verdicts[1] = False
            break
    
    co_ordinates = [i // 3 for i in co_ordinates[1:]]

    for i in range(co_ordinates[0] * 3, (co_ordinates[0] * 3) + 3):
        for j in range(co_ordinates[1] * 3, (co_ordinates[1] * 3) + 3):

            if( board[i][j] == number):

                verdicts[2] = False
                i = 10
                break

    return (False not in verdicts)



def solve_board(board, row):

    co_ordinates = find_slot(board, row)

    if (not co_ordinates[0]):
        return True
    
    for i in range(1, 10):

        if (check_validity(board, co_ordinates, i)):
            board[co_ordinates[1]][co_ordinates[2]] = i

            if (solve_board(board, co_ordinates[1])):

                return board

            board[co_ordinates[1]][co_ordinates[2]] = 0
    
    print("Returning False")
    return False


if __name__ == "__main__":

    board = [
        [0, 0, 9, 0, 0, 5, 0, 1, 0], 
        [0, 8, 5, 1, 0, 0, 3, 4, 0], 
        [0, 0, 7, 0, 4, 2, 0, 0, 8], 
        [0, 5, 0, 0, 2, 1, 8, 6, 0], 
        [0, 0, 6, 5, 0, 0, 2, 0, 0], 
        [8, 0, 0, 0, 6, 4, 5, 9, 0], 
        [0, 0, 0, 0, 5, 3, 0, 0, 0], 
        [4, 0, 0, 8, 7, 6, 1, 3, 5], 
        [0, 0, 0, 0, 1, 0, 0, 0, 0]
    ]

    print_board(solve_board(board, 0))