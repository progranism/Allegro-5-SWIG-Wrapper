from allegro import *

if not al_init():
	print "Error initialising Allegro"
	exit()

al_init_image_addon()

sprite = al_load_bitmap("data/cursor.tga")
if not sprite:
	print "Error loading data/cursor.tga"
	exit()

bmp = al_create_bitmap(256, 256)
if not bmp:
	print "Error creating bitmap"
	exit()

al_set_target_bitmap(bmp)

c1 = al_map_rgb(255, 0, 0)
c2 = al_map_rgb(0, 255, 0)
c3 = al_map_rgb(0, 255, 255)

al_draw_bitmap(sprite, 0, 0, 0)
al_draw_tinted_bitmap(sprite, c1, 64, 0, ALLEGRO_FLIP_HORIZONTAL)
al_draw_tinted_bitmap(sprite, c2, 0, 64, ALLEGRO_FLIP_VERTICAL)
al_draw_tinted_bitmap(sprite, c3, 64, 64, ALLEGRO_FLIP_HORIZONTAL or ALLEGRO_FLIP_VERTICAL)

rc = al_save_bitmap("ex_nodisplay_out.tga", bmp)

if rc:
	print "Saved ex_nodisplay_out.tga"
else:
	print "Error saving ex_nodisplay_out.tga"
	exit()

al_destroy_bitmap(sprite)
al_destroy_bitmap(bmp)

