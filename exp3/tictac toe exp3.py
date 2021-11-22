brd = [
    ['_', '_', '_'],
    ['_', '_', '_'],
    ['_', '_', '_'],
]

finalstate = [
    [(0, 0), (0, 1), (0, 2)],
    [(1, 0), (1, 1), (1, 2)],
    [(2, 0), (2, 1), (2, 2)],
    [(0, 0), (1, 0), (2, 0)],
    [(0, 1), (1, 1), (2, 1)],
    [(0, 2), (1, 2), (2, 2)],
    [(0, 0), (1, 1), (2, 2)],
    [(0, 2), (1, 1), (2, 0)],
]
def calculate_F_Value(i , j):
    maxElement = [-1, -1, -1]
    for _ in finalstate:
        empty = 0
        dot = 0
        cross = 0
        if (i, j) in _:
            for k in _:
                if brd[k[0]][k[1]] == '_':
                    empty += 1
                if brd[k[0]][k[1]] == 'o':
                    dot += 1
                if brd[k[0]][k[1]] == 'x':
                    cross += 1
        if maxElement[2] < cross:
            maxElement = [i, j, cross]
    
    return maxElement 
        

def algo():
    fvalueList = []
    for i in range(3):
        for j in range(3):
            if brd[i][j] == '_':
                brd[i][j] = 'o'
                fvalueList.append(calculate_F_Value(i, j)) 
                brd[i][j] = '_'
    position = max(fvalueList, key=lambda x: x[2])
    brd[position[0]][position[1]] = 'o'

def checkifWon():
    flagH = None
    counter = 0
    for i in range(3):
        for j in range(3):
            if brd[i][j] != '_':
                counter += 1 
    
    # when it's a draw
    if counter == 9:
        flagH = "Draw"

    for location in finalstate:
        
        if brd[location[0][0]][location[0][1]] == 'x' and brd[location[1][0]][location[1][1]] == 'x' and brd[location[2][0]][location[2][1]] == 'x':
            flagH = True
            break
        elif brd[location[0][0]][location[0][1]] == 'o' and brd[location[1][0]][location[1][1]] == 'o' and brd[location[2][0]][location[2][1]] == 'o':
            flagH = False
            break
    return flagH

# function for printing the board
def printboard():
    print(brd[0][0], "|", brd[0][1], "|", brd[0][2])
    print(brd[1][0], "|", brd[1][1], "|", brd[1][2])
    print(brd[2][0], "|", brd[2][1], "|", brd[2][2])
    print("\n\n")
   
end = False
#Print empty board
print("Let's play Tic Tac Toe!!!")

print("You are X !!!")

while True:
    print("Enter your move:")
    row=int(input("Enter the row number"))
    column=int(input("Enter the column number"))
    user = [row,column]
    user = [user[0] - 1, user[1] - 1]
    
    if brd[user[0]][user[1]] != '_':
        print("Play again. The spot is already occupied!!")
        continue

    brd[user[0]][user[1]] = 'x'
    
    print("Your move")
    printboard()
    
    Status = checkifWon()
    if Status == True:
        print("You won the game!!")
        end= True
        break
    elif Status == False:
        print("You lost the game!!")
        end= True
        break
    elif Status == "Draw":
        print("It's a Draw!!")
        end= True
        break
    
    if not end: algo()
    
    print("Computer's move")
    printboard()
    Status = checkifWon()
    if Status == True:
        print("You won the game!!")
        break
    elif Status == False:
        print("You lost the game!")
        break
    elif Status == "Draw":
        print("It's a Draw!")