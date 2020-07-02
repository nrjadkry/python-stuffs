board=["-","-","-",
       "-","-","-",
       "-","-","-"]

def display_board():
  print(board[0]+' | '+board[1]+' | '+board[2])
  print(board[3]+' | '+board[4]+' | '+board[4])
  print(board[6]+' | '+board[7]+' | '+board[8])

def play_game():
  display_board()
  handle_turn()

def handle_turn():
  position=input("Choose a position between 1-9: ")
  position=int(position)-1
  
  board[position]='X'
  display_board()

play_game()#Global Variables

#Game board
board=["-","-","-",
       "-","-","-",
       "-","-","-"]


#If game is still game_is_going_on
game_is_going_on=True

#Who won? or tie?
Winner=None

#Whose turn?
current_player='X'
def display_board():
  print(board[0]+' | '+board[1]+' | '+board[2])
  print(board[3]+' | '+board[4]+' | '+board[5])
  print(board[6]+' | '+board[7]+' | '+board[8])

def play_game():
  display_board()

  while game_is_going_on:

    handle_turn(current_player)

    check_if_game_over()

    flip_player()

  #The game has ended
  if Winner=="X" or Winner=="O":
    print(Winner+' won.')
  elif Winner==None:
    print("Tie.")



  

def handle_turn(player):
  print(player+"'s. turn")
  position=input("Choose a position between 1-9: ")

  valid=False
  while not valid:

    while position not in ['1','2','3','4','5','6','7','8','9']:
      position=input("Choose a number from 1-9: ")
    position=int(position)-1
    
    if board[position]=="-":
      valid=True
    else:
      print("You can't go there. Go again ")
      display_board()



  board[position]=player
  display_board()

def check_if_game_over():
  check_if_win()
  check_if_draw()

def check_if_win():

  #set up global variable
  global Winner
  #check rows
  row_winner=check_rows()

  #check columns
  column_winner=check_columns()

  #check diagonals
  diagonals_winner=check_diagonals()

  if row_winner:
    Winner=row_winner
  elif column_winner:
    Winner=column_winner
  elif diagonals_winner:
    Winner=diagonals_winner
  else:
    Winner=None

  return

def check_rows():

  #Set up global Winner
  global game_is_going_on

  #check if any of the rows have the same value (and is not empty)
  row_1=board[0]==board[1]==board[2]!="-"
  row_2=board[3]==board[4]==board[5]!="-"
  row_3=board[6]==board[7]==board[8]!="-"

  #If any rows have a match, there is a Winner
  if row_1 or row_2 or row_3:
    game_is_going_on=False

  #return the winner(X or O)
  if row_1:
    return board[0]
  elif row_2:
    return board[3]
  elif row_3:
    return board[6]


  return

def check_columns():

    #Set up global Winner
  global game_is_going_on

  #check if any of the column have the same value (and is not empty)
  column_1=board[0]==board[3]==board[6]!="-"
  column_2=board[1]==board[4]==board[7]!="-"
  column_3=board[2]==board[5]==board[8]!="-"

  #If any column have a match, there is a Winner
  if column_1 or column_2 or column_3:
    game_is_going_on=False

  #return the winner(X or O)
  if column_1:
    return board[0]
  elif column_2:
    return board[1]
  elif column_3:
    return board[2]

  return

def check_diagonals():

      #Set up global Winner
  global game_is_going_on

  #check if any of the diagonal have the same value (and is not empty)
  diagonal_1=board[0]==board[4]==board[8]!="-"
  diagonal_2=board[2]==board[4]==board[6]!="-"
 

  #If any diagonal have a match, there is a Winner
  if diagonal_1 or diagonal_2:
    game_is_going_on=False

  #return the winner(X or O)
  if diagonal_1:
    return board[0]
  elif diagonal_2:
    return board[2]


  return

def check_if_draw():
  global game_is_going_on
  if "-" not in board:
    game_is_going_on=False

  return

def flip_player():

  #Set up a global variable
  global current_player

  if current_player=="X": # double equals is used to check
    current_player="O"    # single equals is used to assign
  elif current_player=="O":
    current_player="X"

  return

play_game()