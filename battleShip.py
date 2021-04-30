'''                                         INSTRUCTIONS 
        The user will have to enter the grid size (n) and the ship size (s) and the ship will be placed horizontally or vertically at any random position.
        A  n x n board will be printed in which :
        - the places with 'O' represent the coordinates that are untouched.
        - the places with '-' represent the coordinates given by the user that were unsuccessful.
        - the places with 'X' represent the coordinates given by the user that were successful  
           The user will have to enter the desired coordinate after which that coordinate will be represented in one of the three ways above mentioned.
           '''
import random

n = int(input('Enter the grid size (min = 5, max = 10) : '))

while n not in range(5,11):
    print('Enter the integer in the specified range.')
    del n
    n = int(input('Enter the grid length (min = 5, max = 10) : '))

s = int(input('Enter the ship length (min = 3,max = {}) : '.format(n)))
while s not in range(3,n+1):
    print('Enter the integer in the specified range.')
    del s
    s = int(input('Enter the ship length (min = 3,max = {}) : '.format(n)))


# defining a list that will hold the grid elements.
# elements are stored in form of lists so that we can change them in future when required
board = [list('O')*n for i in range(n)]

# initializing a variable that will hold the number of chances.
chance_count = 0

# var that will store the number of hits.
hit_count = 0

#  1 - horizontal  2 - vertical
ship_orientation = random.randint(1,2)

# defining a function that will display the board in form of a grid.
def grid_board(board):
    print()
    for i in range(n):
        for j in range(n):
            print(board[i][j],end=' ')
        print()
    print()    

# assigning the ship coordinates :
if ship_orientation == 1 :
    c1_row = random.randint(0,n-1)
    c1_coloumn = random.randint(0,n-s)
    # orientation of the ship is horizontal, so the initial coloumn can be 3 at max. 
    ship_coordinates = [(c1_row ,c1_coloumn + i) for i in range(s)]
elif ship_orientation == 2 :
    c1_row = random.randint(0,n-s)    
    c1_coloumn = random.randint(0,n-1)   
    ship_coordinates = [(c1_row + i ,c1_coloumn ) for i in range(s)]

# main code
while chance_count <= n**2:
    
    grid_board(board)
    row = int(input('enter the row number (0 - {} ) : '.format(n-1)))
    coloumn = int(input('enter the coloumn number (0 - {} ) : '.format(n-1)))
    print()

    if row<0 or row > n-1 or coloumn<0 or coloumn>n-1 :
        print('Enter a valid coordinate inside the range 0 - 5 . ') 

    elif (row,coloumn) in ship_coordinates:
        board[row][coloumn] = 'X'
        chance_count += 1
        hit_count+= 1 
        if hit_count == s:
            grid_board(board)
            print('You win!')
            print('You took',chance_count,'chances.')
            break
        else:
            continue 
        
    elif (row,coloumn) not in ship_coordinates:
        if board[row][coloumn] =='-':
            print('You have already entered this coordinate, enter any other coordinate.') 
            print()   
        else :
            board[row][coloumn] = '-'
            chance_count += 1 
