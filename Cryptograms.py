# ============================================================
#
# Student Name (as it appears on cuLearn): Umar Farooq
# Student ID (9 digits in angle brackets): <101094104>
# Course Code (for this current semester): COMP1405A
#
# ============================================================
'''
This function will load a text file.

@params 	file_name, the name of the file to be loaded

@return 	an uppercase string containing the data read from the file

'''

def load_text(file_name):
	file_hnd1 = open(file_name, "r")
	file_data = file_hnd1.read()
	file_hnd1.close()
	return file_data.upper()

'''
This function will save data to a text file.

@params 	file_name, the name of the file to be saved
		file_data, the data to be written to the file

@return		none

'''

def save_text(file_name, file_data):
	file_hnd1 = open(file_name, "w")
	file_hnd1.write(file_data)
	file_hnd1.close()


'''
This function will create alphabet which is shifted.

@params 	shift_value, integer value which will make the alphabet to be shifted

@return 	caesar, alphabet that is shifted by the shift_value

'''

def caesar_cipher_alphabet(shift_value):
	alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	caesar = ""
	
	for i in range(shift_value,len(alpha)): #start with the shifting value and end to the last letter
		caesar += alpha[i]
		
	for j in range(0,shift_value): #start with the first letter up until the shifting value
		caesar += alpha[j]
	
	return caesar


'''
This function will move the the letters from a keyword to the beginning of the alphabet without changing their order.

@params 	keyword, cipher alphabet which move letters, that user wants from alpha(variable) to the beginning without changing their order and the duplicates are used once.

@return 	final_alpha, which is the keyword that has a new alphabet. For eg: ROBETACDFGHIJKLMNPQSUVWXYZ

'''


def keyword_cipher_alphabet(keyword):
	alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	keyword_2 = ""
	alpha_2 = ""
	
	duplicate = False
	#we look for duplicates within the keyword
	for i in keyword:
		for j in keyword_2:
			if i == j:
				duplicate=True
		if not duplicate:
			keyword_2 += i
		duplicate = False
	
	#we look for the letters of the keyword within the alphabet
	duplicate = False
	for i in alpha:
		for j in keyword_2:
			if i == j:
				duplicate=True
		if not duplicate:
			alpha_2 += i
		duplicate = False
	
	#we add the keyword without duplicates with the alphabets without the keyword letters
	final_alpha = keyword_2+alpha_2
	
	return final_alpha


'''
This function will use input to ask the user to type an alphabet. If the alphabet contains 26 letters with no duplicate, this function will returns those 26 letters. But if it contains less than 26 letters and/or duplicates then it will print an error and returns default 26 letters.

@params 	none

@return 	user_alpha, which has 26 English alphabet letters and contains no duplicates.
		real_alpha, which is the unmodified alphabet of 26 letters (default).

'''
	
def cryptogram_alphabet():
	user_alpha = (input("\nEnter your cryptogram alphabet: ")).upper()
	
	real_alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	
	user_alpha_2 = ""
	
	if len(user_alpha) == 26: #first check if input is of length 26
	
		#we check if any duplicates are within the user input
		duplicate = False 
		for i in user_alpha:
			for j in user_alpha_2:
				if i == j:
					duplicate=True
		#if there is, return the normal alphabet otherwise return the input
		if duplicate:
			print("\nError not a cryptogram alphabet.")
			return real_alpha
		else:
			return user_alpha
	
	else:
		print("\nError not a cryptogram alphabet.")
		return real_alpha



'''
This function will encode.

@params 	text, that program most recently created by encoding
		alphabet, the current alphabet which is being used for encoding

@return 	the return value will be the encoded_text

'''
		
def encode(text, alphabet):
	encoded_text = "" # encoded text which will be returned
	
	real_alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	
	for char in text:
		
		if ord(char)<65 or ord(char)>90:  #check if the character is NOT a letter
			encoded_text += char #if not a letter add it to the encoded text
		else: 
			index_char = 0 #find the index within the real alphabet
			for letter in real_alpha:
				if letter == char:
					break
				else:
					index_char += 1
			encoded_text += alphabet[index_char] #convert the letter value with the index found
			
	return encoded_text.upper()
	

'''
This function will decode.

@params 	text, that program most recently created by encoding
		alphabet, the current alphabet which is being used for encoding

@return 	the return value will be the decoded_text

'''

	
def decode(text, alphabet):
	decoded_text = "" # decoded text which will be returned
	
	real_alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	
	for char in text:
		
		if ord(char)<65 or ord(char)>90:  #check if the character is NOT a letter
			decoded_text += char
		else: 
			index_char=0 #find the index within the cipher alphabet
			for letter in alphabet:
				if letter == char:
					break
				else:
					index_char += 1
			decoded_text += real_alpha[index_char] #convert the letter value with the index found
			
	return decoded_text.upper()

	
'''
This is the main function, responsible for the user interface.

@params 	none

@return 	none

'''

def main():
	
	initial = "" #from load file

	current = "" #from the encode/decode calls

	alphabet = "" #from caesar, cryptogram and keyword alphabet
	
	flag = True # boolean for the menu loop where it will keep displaying until user quits
	
	while flag:
		print("\n============ MENU =============\n\n") #Menu text
		print("Choose of the following options:\n\n")
		print("1. Load file\n")
		print("2. Caesar alphabet\n")
		print("3. Cryptogram alphabet\n")
		print("4. Keyword cipher alphabet\n")
		print("5. Encode\n")
		print("6. Decode\n")
		print("7. Save file\n")
		print("8. Quit\n\n")
		print("===============================\n\n")
		
		selection = int(input("Make a selection with a number: "))
		
		if selection == 1:
			file_name = input("\nPlease enter the file name you want to load: ") #load file
			initial = load_text(file_name) #set the file data to initial
			print("\nYour initial text is: ",initial)
			print("\nYour current text is: ",current)
			print("\nYour alphabet is: ",alphabet)
		elif selection == 2:
			shifting = int(input("\nEnter the shift value for the caesar alphabet: ")) #get input for shift value
			alphabet = caesar_cipher_alphabet(shifting) #function returns and sets the alphabet
			print("\nYour initial text is: ",initial)
			print("\nYour current text is: ",current)
			print("\nYour alphabet is: ",alphabet)
		elif selection == 3:
			alphabet = cryptogram_alphabet() #function get input from user and sets the alphabet
			print("\nYour initial text is: ",initial)
			print("\nYour current text is: ",current)
			print("\nYour alphabet is: ",alphabet)
		elif selection == 4:
			keyword = input("\nEnter the keyword for the keyword alphabet: ") #get input for shift value
			alphabet = keyword_cipher_alphabet(keyword.upper()) #function returns and sets the alphabet
			print("\nYour initial text is: ",initial)
			print("\nYour current text is: ",current)
			print("\nYour alphabet is: ",alphabet)
		elif selection == 5 or selection == 6:
			if initial == "":
				print("\nPlease load a file before proceeding.")
			elif alphabet == "":
				print("\nPlease make an alphabet through the menu options before proceeding.")
			else:
				if selection == 5:
					current=encode(initial,alphabet) #function returns and sets current
					print("\nYour initial text is: ",initial)
					print("\nYour current text is: ",current)
					print("\nYour alphabet is: ",alphabet)
				else:
					current = decode(initial,alphabet) #function returns and sets current
					print("\nYour initial text is: ",initial)
					print("\nYour current text is: ",current)
					print("\nYour alphabet is: ",alphabet)
		elif selection == 7:
			file_name = input("\nPlease enter the file name you want to save the current text: ") #get input of file name
			if current == "":
				print("\nNo current text available.")
			else:
				save_text(file_name,current) #save the current variable to the file name from the input 
				print("\nYour file was saved successfully to ",file_name)
			print("\nYour initial text is: ",initial)
			print("\nYour current text is: ",current)
			print("\nYour alphabet is: ",alphabet)
		elif selection == 8:
			print("\nThank you for using the cryptogram. Have a nice day! :)")
			flag = False #break loop after quitting


main()


