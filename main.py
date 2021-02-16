board = [[9, 0, 0, 6, 0, 0, 3, 0, 0],
         [0, 0, 0, 0, 0, 0, 4, 6, 9],
         [6, 0, 0, 5, 4, 0, 0, 0, 0],
         [3, 7, 8, 0, 0, 5, 0, 0, 2],
         [0, 0, 0, 7, 6, 3, 0, 1, 5],
         [0, 6, 0, 0, 2, 8, 7, 0, 4],
         [0, 3, 0, 1, 5, 7, 9, 0, 6],
         [0, 4, 5, 3, 0, 0, 1, 2, 0],
         [1, 0, 0, 0, 8, 0, 5, 0, 0]]


def print_board(bo):
    for i in range(9):

        if i % 3 == 0 and i != 0:
            print('----------------------')
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print('|', end=' ')
            print(bo[i][j], end=' ')

        print()


def find_space(bo):
    for i in range(9):
        for j in range(9):
            if bo[i][j] == 0:
                return i, j
    return False


def valid(bo, value, row, col):
    # row
    if value in bo[row]:
        return False

    # col
    for i in range(9):
        if bo[i][col] == value:
            return False

    # 3x3 box

    r = row // 3 * 3
    c = col // 3 * 3
    for i in range(r, r + 3):
        for j in range(c, c + 3):
            if bo[i][j] == value and (i, j) != (row, col):
                return False
    return True


def solve(bo):
    # print('\ninitial Board')
    # print('----------------------------\n')
    # print(bo)

    find = find_space(bo)
    if not find:
        return True

    else:
        row, col = find

    for i in range(1, 10):
        if valid(bo, i, row, col):
            bo[row][col]=i

            if solve(bo):
                return True
            bo[row][col] = 0

    return False


print_board(board)
solve(board)
print('----------------------------------------------------------------')
print_board(board)
