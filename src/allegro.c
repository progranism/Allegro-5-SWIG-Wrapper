#include <allegro5/allegro5.h>
//#include <stdbool.h>
//

#undef al_init

bool al_init()
{
	return al_install_system(ALLEGRO_VERSION_INT, NULL);
}

