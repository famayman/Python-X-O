from random import randrange
def printboard(board):
   k=0
   for i in range (4):
       print("+"+"-------"+"+"+"-------"+"+"+"-------"+"+")
       if i==3:
          continue
       for j in range (3):

           print("|   ",end='')
           if j == 1:
               print(board[k][0],end='')
           else:
               print(' ',end='')
           print("   |   ",end='')
           if j == 1:
               print(board[k][1],end='')
           else:
               print(' ',end='')
           print("   |   ",end='')
           if j == 1:
               print(board[k][2],end='')
               k=k+1
           else:
               print(' ',end='')

           print( "   |      ")
def enter_move(board):

    n=int(input("Enter your move "))
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == n:
                board[i][j] = "O"
def  pc_move(board):
    computer_turn = True
    while computer_turn:
        k=randrange(10)
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == k:
                    board[i][j]= "X"
                    computer_turn=False
    printboard(board)
def list_of_free_fields(board):
    mylist=[]
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == "X" or board[i][j] == "O":
                continue
            else:
                mylist.append((i,j))
    if mylist ==[]:
        return True
def victory_for(board, sign):
    global ok
    ok = sign
    X1=0
    X2=0
    X3=0
    X4=0
    for i in range (3):
        for j in range (3):
            if board[i][j] == sign:
                X1+=1
                if X1 == 3 :
                    return sign
            if board[j][i] == sign:
                X2+=1
                if X2 == 3:
                     return sign
        X1 = 0
        X2 = 0

        if board[i][i] == sign:
            X3+=1
            if X3 == 3:
                return sign
        if board[i][3-i-1] == sign:
            X4+=1
            if X4 == 3:
                return sign
def draw_move(board):
    newlist=[]
    if list_of_free_fields(board):
         return True

board=[[1,2,3],[4,"X",6],[7,8,9]]
printboard(board)
for i in range (9):
    enter_move(board)
    if victory_for(board,"X") == ok:
        print("X wins")
        break
    if victory_for(board,"O") == ok:
        print("O wins")
        break
    printboard(board)
    pc_move(board)
    if victory_for(board,"X") == ok:
        print("X wins")
        break
    if victory_for(board,"O") == ok:
        print("O wins")
        break
    if draw_move(board):
        print("None wins")
        break
