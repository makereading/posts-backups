import pygame

# global variables
width = 600
height = 400

#initialization of pygame screen
pygame.init()

screen = pygame.display.set_mode((width, height))

#animation loop
animating = True
while animating:

	# actual animation
	x = 200
	y = 100
	bar_width = 100


	# track user interation
	for event in pygame.event.get():

		# User closes the pygame
		if event.type == pygame.QUIT:
			animating = False