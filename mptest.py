# # # # #
# CONSTANTS

DUMMY = False
RES = (640,480)


# # # # #
# IMPORTS

# external
import pygame

# custom
if not DUMMY:
	from libmpdev import MP150


# # # # #
# STARTUP

# initialize PyGame
pygame.init()

# create a new display
disp = pygame.display.set_mode(RES, pygame.RESIZABLE)

# font to display text
font = pygame.font.Font(pygame.font.get_default_font(), 24)

# start communication with the squeezies
if not DUMMY:
	mp = MP150()


# # # # #
# RUN

# run until quited
quited = False
while not quited:

	# start recording
	if not DUMMY:
		mp.start_recording()

	# get new squeezie sample
	if not DUMMY:
		sample = mp.sample()
	else:
		sample = 'dummymode'

	# render text
	textsurf = font.render("sample = %.3f, %.3f, %.3f" % (sample[0], sample[1], sample[2]), False, (255,255,255))
	blitpos = (int(RES[0]/2 - textsurf.get_width()/2), int(RES[1]/2 - textsurf.get_height()/2))
	
	# blit text to display
	disp.fill((0,0,0))
	disp.blit(textsurf, blitpos)
	
	# update display
	pygame.display.flip()
	
	# check if there was any keyboard input
	for event in pygame.event.get(pygame.KEYDOWN):
		if pygame.key.name(event.key) == 'escape':
			quited = True

# start recording
if not DUMMY:
	mp.stop_recording()


# # # # #
# CLOSE

# close connection to MP150
if not DUMMY:
	mp.close()

# close the display
pygame.display.quit()