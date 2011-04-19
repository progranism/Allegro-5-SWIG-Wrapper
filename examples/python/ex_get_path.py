from allegro import *


def show_path(id, label):
	path = al_get_standard_path(id)
	if path:
		path_str = al_path_cstr(path, ALLEGRO_NATIVE_PATH_SEP)
	else:
		path_str = "<none>"
	print label, ": ", path_str
	al_destroy_path(path)


al_set_org_name("liballeg.org")

al_set_app_name("ex_get_path")

if not al_init():
	print "Could not init Allegro."
	exit()

show_path(ALLEGRO_RESOURCES_PATH, "RESOURCES_PATH");
show_path(ALLEGRO_TEMP_PATH, "TEMP_PATH");
show_path(ALLEGRO_USER_DATA_PATH, "USER_DATA_PATH");
show_path(ALLEGRO_USER_SETTINGS_PATH, "USER_SETTINGS_PATH");
show_path(ALLEGRO_USER_HOME_PATH, "USER_HOME_PATH");
show_path(ALLEGRO_USER_DOCUMENTS_PATH, "USER_DOCUMENTS_PATH");
show_path(ALLEGRO_EXENAME_PATH, "EXENAME_PATH");

