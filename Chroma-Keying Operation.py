# ============================================================
#
# Student Name (as it appears on cuLearn): Umar Farooq
# Student ID (9 digits in angle brackets): <101094104>
# Course Code (for this current semester): COMP1405A
#
# ============================================================

import pygame

from pygame.locals import *

# Initialize the pygame

pygame.init()

# Ask the user if they require instructions

instruction_question = input("Do you need instructions? ")

if instruction_question.upper() == "YES":
	
	print("Need to merge two images.")

	print("The first image will be a background image.")

	print("The second image will be the image of a ghost against a green background.")

	print("Make sure image name ends with .bmp or if you are using your own files make sure the filename you enter is correct.")

	print("Provide coordinates to center the ghost image.")

	print("Make sure these coordinates are within the background width and height.")

# Ask user to enter the filename of their desired background image and ghost image and also load an image and store the surface in the variable background_image and ghost_image

ghost_image = pygame.image.load(input("Enter the file name of the ghost image: "))

background_image = pygame.image.load(input("Enter the file name of the background image: "))

# Get the dimensions of the background_image, where w = width and h = height 

(w, h) = background_image.get_rect().size

# Display the background image

drawing_window = pygame.display.set_mode( (w, h) )

# Copying background_image onto drawing_window

drawing_window.blit(background_image, (0, 0))

# Get the dimensions of the ghost_image, where gw = ghost width and gh = ghost height

(gw, gh) = ghost_image.get_rect().size

# Ask the user for the x and y coordinates

x = int(input("Enter the x coordinate at which you want to center the ghost: "))

while (x < 0 or x > w):

	x = int(input("Invalid coordinate(s), please enter the x coordinate within the background width: "))


y = int(input("Enter the y coordinate at which you want to center the ghost: "))

while (y < 0 or y > h):

	y = int(input("Invalid coordinate(s), please enter the y coordinate within the background height: "))

# Check each pixel from the ghost image and see if that pixel is green or not

for i in range(0, gw, 1):
	
	for j in range(0, gh, 1):
		
		# br, bg, bb are assigned the background color pixels and gr, gg, gb are assigned the ghost color pixels

		if (((i + x) < w) and ((j + y) < h)):
			
			(br, bg, bb, _) = background_image.get_at( (i + x, j + y) )

			(gr, gg, gb, _) = ghost_image.get_at( (i, j) )

			# Average the red, green, and blue values of the non-green pixel from the ghost image with the pixel from the background image

			redAv = (br + gr)/2

			greenAv = (br + gr)/2

			blueAv = (br + gr)/2

			color = (redAv, greenAv, blueAv)		

		if (gr, gg, gb, _) == (0, 255, 0, _):

			ghost_image.set_at( (i, j), (br, bg, bb)) 

		else:

			ghost_image.set_at( (i, j), color)
		
	
drawing_window.blit(ghost_image, (x, y))

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
	pygame.display.update()











 
