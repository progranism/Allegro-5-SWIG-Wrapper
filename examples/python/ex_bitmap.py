import sys
from allegro import *

if len(sys.argv) > 1:
	filename = sys.argv[1]
else:
	filename = "data/mysha.pcx"

if not al_init():
	print "Could not init Allegro."
	exit()

if len(sys.argv) > 2:
	al_set_new_display_adapter(int(argv[2]))

al_install_mouse()
al_install_keyboard()

al_init_image_addon()

display = al_create_display(640, 480)
if not display:
	print "Error creating display"
	exit()

al_set_window_title(display, filename)

al_set_new_bitmap_flags(ALLEGRO_MEMORY_BITMAP)
t0 = al_get_time()
membitmap = al_load_bitmap(filename)
t1 = al_get_time()

if not membitmap:
	print filename, "not found or failed to load"
	exit()

al_set_new_bitmap_flags(ALLEGRO_VIDEO_BITMAP)

print "Loading took", (t1 - t0), " seconds"

bitmap = al_clone_bitmap(membitmap)
if not bitmap:
	bitmap = membitmap

timer = al_create_timer(1.0 / 30)
queue = al_create_event_queue()
al_register_event_source(queue, al_get_keyboard_event_source())
al_register_event_source(queue, al_get_display_event_source(display))
al_register_event_source(queue, al_get_timer_event_source(timer))
al_start_timer(timer)

redraw = False
zoom = 1

while True:
	event = ALLEGRO_EVENT()
	al_wait_for_event(queue, event)

	if event.type == ALLEGRO_EVENT_DISPLAY_CLOSE:
		break
	elif event.type == ALLEGRO_EVENT_KEY_CHAR:
		if event.keyboard.keycode == ALLEGRO_KEY_ESCAPE:
			break
		elif chr(event.keyboard.unichar) == '1':
			zoom = 1
		elif chr(event.keyboard.unichar) == '+':
			zoom *= 1.1
		elif chr(event.keyboard.unichar) == '-':
			zoom /= 1.1
		elif chr(event.keyboard.unichar) == 'f':
			zoom = al_get_display_width(display) / al_get_bitmap_width(bitmap)
	elif event.type == ALLEGRO_EVENT_TIMER:
		redraw = True
	
	if redraw and al_is_event_queue_empty(queue):
		redraw = False
		al_clear_to_color(al_map_rgb_f(0, 0, 0))
		if zoom == 1:
			al_draw_bitmap(bitmap, 0, 0, 0)
		else:
			al_draw_scaled_rotated_bitmap(bitmap, 0, 0, 0, 0, zoom, zoom, 0, 0)
		al_flip_display()


al_destroy_bitmap(bitmap)

