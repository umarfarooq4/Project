# ============================================================
#
# Student Name (as it appears on cuLearn): Umar Farooq
# Student ID (9 digits in angle brackets): <101094104>
# Course Code (for this current semester): COMP1405A
#
# ============================================================

'''
This function set the board through asking the user to enter characters in row 1 to 8. 
Then, it checks if the user enter the correct characters in each row specified by a variable "valid_char".
It also checks the length of the characters, defined in the variable valid_char, in row 1 to 8. 
Correct length is 8. Anything below or above will output an error.

@params 	none

@return 	board, as a list of lists of characters

'''

def boardSet ():
	board = []
	valid_char = "KQRNBPkqrnbp-"

	for i in range (8):

		invalid_row = True

		while(invalid_row):

			row = input("\nEnter row "+str((i+1))+" of 8 with eight characters containing: ")

			for j in row:

				if j in valid_char:
					invalid_row = False

				else:
					invalid_row = True
					print("\nERROR 1: The row contains invalid characters.")
					break

			if len(row)==8 and invalid_row==False:
				invalid_row = False

			elif not len(row)==8:
				invalid_row = True
				print("\nERROR 2: The row length is not 8.")
		
		row_list = list(row)
		
		board.append(row_list)
				
	return board

'''
This function takes the board which was set by the user and determines the score of "Black" and "White".
Black chess pieces are represented by upercase letters.
White chess pieces are represented by lowercase letters.

@params 	board, as a list of characters

@return 	score_list, score values of "Black" and "White"

'''

def score (board):
	black_score = 0.0
	white_score = 0.0
	score_list = []
	
	for x in range (0,8):	
	
		for y in range (0,8):

			if(board[x][y]=='Q'):
				black_score +=10.0

			elif(board[x][y]=='R'):
				black_score +=5.0

			elif(board[x][y]=='N'):
				black_score +=3.5

			elif(board[x][y]=='B'):
				black_score +=3

			elif(board[x][y]=='P'):
				black_score +=1
				
			elif(board[x][y]=='q'):
				white_score +=10.0

			elif(board[x][y]=='r'):
				white_score +=5.0

			elif(board[x][y]=='n'):
				white_score +=3.5

			elif(board[x][y]=='b'):
				white_score +=3

			elif(board[x][y]=='p'):
				white_score +=1
	
	score_list.append(black_score)
	score_list.append(white_score)
	
	return score_list
	
'''
This function takes the board which was set by the user and ask the user if he/she wants to move the pieces which were displayed in the original board.
Valid move is followed by inputting coordinates which starts from A-H, ends with a number 1-8 and has a chess piece, in example B2 which has K.
Any other coordinates will result in an error.
At first it will ask the user which chess piece(KQRNBP, kqrnbp) he/she wants to move.
Then ask the user for the distination coordinates of the move. 
Then the function will return the updated board and display the new score of Black and White and show if the score is tied or not.

@params 	board, as a list of characters

@return 	board, which is the updated board showing user's new moves

'''
	
def movePiece(board):
	invalid_xy = True
	point_i = []
	
	# This while loop ask the user for the coordinates of the piece that he/she wants to move and checks if the user entered the correct coordinates of the piece.
	# If wrong corrdinates are inputted, error will appear on to the screen which will ask the user to enter the correct coordinates.
	# This while loop will end when user enter the correct coordinates
	
	while(invalid_xy):

		point_intial = input("\nEnter the coordinates of the piece you want to move (Starts with letter A-H followed by a number 1-8, ex: C6): ")
		
		if len(point_intial)==2:
			point_i = list(point_intial)

		else:
			print("\nERROR 3: Invalid coordinates length must be of length 2 (Starts with A-H followed by 1-8, ex: C6).")
			continue
	
		
		if ord(point_i[0].upper())<65 or ord(point_i[0].upper())>72:
			print("\nERROR 3: First coordinate must contain a letter between A-H.")
		elif ord(point_i[1])<49 or ord(point_i[1])>56:
			print("\nERROR 4: Second coordinate contain a number between 1-8.")
		elif board[ord(point_i[0].upper())-65][ord(point_i[1])-49]=='-':
			print("\nERROR 5: There is no piece at the given position, please choose another coordinate.")
		else:
			invalid_xy = False
	

	print("\nYou are moving the piece "+board[ord(point_i[0].upper())-65][ord(point_i[1])-49]+" from position "+point_i[0].upper()+point_i[1]+".")
		
	invalid_xy_2 = True
	
	# This while loop ask the user for the distination coordinates of the piece and checks if the user entered the correct distination coordinates.
	# If wrong corrdinates are inputted, error will appear on to the screen which will ask the user to enter the correct distination coordinates.
	# This while loop will end when user enter the correct distination coordinates
	
	while(invalid_xy_2):

		point_final = input("\nEnter the coordinates of the destination of "+board[ord(point_i[0].upper())-65][ord(point_i[1])-49]+": ")
		if len(point_final)==2:
			point_final = list(point_final)
		else:
			print("\nERROR 3: Invalid coordinates length must be of length 2 (Starts with A-H followed by 1-8, ex: C6).")
			continue
			
		if ord(point_final[0].upper())<65 or ord(point_final[0].upper())>72:
			print("\nERROR 3: First coordinate must contain a letter between A-H.")
		elif ord(point_final[1])<49 or ord(point_final[1])>56:
			print("\nERROR 4: Second coordinate contain a number between 1-8.")
		else:
			piece = board[ord(point_i[0].upper())-65][ord(point_i[1])-49]
			board[ord(point_i[0].upper())-65][ord(point_i[1])-49]="-"
			board[ord(point_final[0].upper())-65][ord(point_final[1])-49] = piece

			break
		
	return board


'''
This is the main function, responsible for the user interface.

@params 	none

@return 	none

'''

def main ():
	flagGame = True
	currentBoard = False
	board = []
	score_list = []
	
	while(flagGame):	
		print("\n===== Chess game instruction =====")
		print("\nYou will have to build a game with 8 rows and columns.")
		print("\nWhite pieces are lowercase k (for King)...")
		print("\nBlack pieces are uppercase K (for King)...")
		print("\nHyphen (-) is the empty space")
		print("\nAfter the board is valid set the score is calculated and user can set a new board or move a piece.\n\n\n")
	
		print("Options (please choose number 1 to 3):")
		print(" 1) Set new board")
		print(" 2) Move piece")
		print(" 3) Quit\n\n")
		
		if(currentBoard):
			print("Current board: \n")
			char_start = 65
	
			print("\n  12345678")
	
			for x in range (0,8):
				print(chr(char_start+x)+" ", end="")
				
				for y in range (0,8):
					print(board[x][y], end="")
		
				print()
				
			score_list = score(board)
			print("\nBlack score: ",score_list[0])
			print("White score: ",score_list[1])
			
			if score_list[0]>score_list[1]:
				print("Black player is winning.")
			elif score_list[0]<score_list[1]:
				print("White player is winning.")
			else:
				print("The game is tie!")

			
		else:
			print("Current board: No board is set")
	
		selection = input("\nEnter selection: ")
		
		if selection=='1':
			currentBoard = True
			board = boardSet()
			
			char_start = 65
	
			print("\n  12345678")
	
			for x in range (0,8):
				print(chr(char_start+x)+" ", end="")
				
				for y in range (0,8):
					print(board[x][y], end="")
		
				print()
				
			score_list = score(board)
			print("\nBlack score: ",score_list[0])
			print("White score: ",score_list[1])	
			
		elif selection=='2':
			if currentBoard == False:
				print("\nPlease set a new board by entering selection 1.")
			else:
				movePiece(board)
		elif selection=='3':
			print("\nThank you for playing the chess game, have a nice day :)")
			flagGame = False
		else:
			print("\nPlease make a selection between 1 and 3.")


main()
