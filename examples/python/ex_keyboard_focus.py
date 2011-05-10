from allegro import *

def redraw(color1, color2):
	al_set_target_backbuffer(display1)
	al_clear_to_color(color1)
	al_flip_display()

	al_set_target_backbuffer(display2)
	al_clear_to_color(color2)
	al_flip_display()

if not al_init():
	print "Error initialising Allegro."
	exit()

if not al_install_keyboard():
	print "Error installing keyboard."
	exit()

display1 = al_create_display(300, 300)
display2 = al_create_display(300, 300)
if not display1 or not display2:
	print "Error creating displays."
	exit()

black = al_map_rgb(0, 0, 0)
red = al_map_rgb(255, 0, 0)

kbdstate = ALLEGRO_KEYBOARD_STATE()

while True:
	al_get_keyboard_state(kbdstate)
	if al_key_down(kbdstate, ALLEGRO_KEY_ESCAPE):
		break

	if kbdstate.display == display1:
		redraw(red, black)
	elif kbdstate.display == display2:
		redraw(black, red)
	else:
		redraw(black, black)
	
	al_rest(0.1)



