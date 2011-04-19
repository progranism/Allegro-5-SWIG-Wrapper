from allegro import *
import sys

if len(sys.argv) < 3:
	print "Usage: ex_convert <infile> <outfile>"
	print "\tPossible file types: BMP PCX PNG TGA"
	exit()

if not al_init():
	print "Could not init Allegro."
	exit()

al_init_image_addon()

al_set_new_bitmap_format(ALLEGRO_PIXEL_FORMAT_ARGB_8888)
al_set_new_bitmap_flags(ALLEGRO_MEMORY_BITMAP | ALLEGRO_NO_PREMULTIPLIED_ALPHA)

bitmap = al_load_bitmap(sys.argv[1])

if not bitmap:
	print "Error loading input file"
	exit()


t0 = al_get_time()
if not al_save_bitmap(sys.argv[2], bitmap):
	print "Error saving bitmap"
	exit()

t1 = al_get_time()

print "Saving took", (t1 - t0), "seconds"

al_destroy_bitmap(bitmap)



