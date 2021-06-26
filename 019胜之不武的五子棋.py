import random

black_xs = []
black_ys = []

# define size of board
BOARD_SIZE = 15
# define a 2D list as board
board = []

def initBoard():
    # default every element as '+' to draw the board
    for i in range(BOARD_SIZE):
        row = ["＋ "] * BOARD_SIZE
        board.append(row)

# draw the board
def printBoard():
    print("  ", end='')
    for i in range (1, BOARD_SIZE+1):
        print ("%02d" % i, end=' ')
    print()
    # print every element
    for i in range(BOARD_SIZE):
        print("%02d" % (i+1), end='')
        for j in range(BOARD_SIZE):
            print(board[i][j], end='')
        print() # 打印完一行后换行

def legitimate_move(x, y):
    if x > 15 or y >15 or board[x][y] != "＋ " :
        print("输入错误")
        return False
    else:
        return True

def black_play():
    inputStr = input("请输入您下棋的坐标，应以x, y(表示列,行)的格式：\n")
    x_str, y_str = inputStr.split(sep=",")
    x = int(x_str) -1
    y = int(y_str)-1
    if legitimate_move(x, y):
        board[x] [y] ="黑 "
        black_xs.append(x)
        black_ys.append(y)
    else:
        black_play()
    printBoard()
    
def white_play():
    x = random.randint(0,14)
    y = random.randint(0,14)
    while not legitimate_move(x, y):
        x = random.randint(0,14)
        y = random.randint(0,14)
    board[x] [y] ="白 "
    printBoard()
    
def black_win():
    if black_xs[0]==black_xs[1]:
        if black_xs[0]==black_xs[2]:
            if black_xs[0]==black_xs[3]:
                if black_xs[0]==black_xs[4]:
                    return True
    elif black_ys[0]==black_ys[1]:
        if black_ys[0]==black_ys[2]:
            if black_ys[0]==black_ys[3]:
                if black_ys[0]==black_ys[4]:
                    return True
    elif (black_xs[0] - black_ys[0]) == (black_xs[1] - black_ys[1]):
        if (black_xs[0] - black_ys[0]) == (black_xs[2] - black_ys[2]):
            if (black_xs[0] - black_ys[0]) == (black_xs[3] - black_ys[3]):
                if (black_xs[0] - black_ys[0]) == (black_xs[4] - black_ys[4]):
                    return True
    elif (black_xs[0] + black_ys[0]) == (black_xs[1] + black_ys[1]):
        if (black_xs[0] + black_ys[0]) == (black_xs[2] + black_ys[2]):
            if (black_xs[0] + black_ys[0]) == (black_xs[3] + black_ys[3]):
                if (black_xs[0] + black_ys[0]) == (black_xs[4] + black_ys[4]):
                    return True
    else:
        return False

initBoard()
printBoard()

for i in range (5):
    black_play()
    white_play()
if black_win():
    print("You win!")
else:
    print("You lose.")    

    
