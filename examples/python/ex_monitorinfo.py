from allegro import *

if not al_init():
	print "Could not init Allegro."
	exit()

num_adapters = al_get_num_video_adapters()

print num_adapters, "adapters found..."


for i in range(0, num_adapters):
	info = ALLEGRO_MONITOR_INFO()
	al_get_monitor_info(i, info)

	print "Adapter", i, ": ", info.x1, info.y1, info.x2, info.y2
	
	al_set_new_display_adapter(i)
	print "     Available fullscreen display modes:"

	for j in range(0, al_get_num_display_modes()):
		mode = ALLEGRO_DISPLAY_MODE()

		al_get_display_mode(j, mode)

		print "     Mode ", j, mode.width, mode.height, mode.refresh_rate



