%module allegro

%{
        #include <allegro5/allegro5.h>
        #include <allegro5/internal/alconfig.h>
        #include <allegro5/allegro_image.h>
        #include <allegro5/allegro_primitives.h>
        #undef al_init
%}


%define AL_FUNC(type, name, args)
type name args
%enddef

/*%define ALLEGRO_IIO_FUNC(type, name, args)
extern type name args
%enddef*/


extern bool al_init();


%ignore al_init;
//%ignore ALLEGRO_IIO_FUNC

%include <allegro5/system.h>
%include <allegro5/display.h>
%include <allegro5/color.h>
%include <allegro5/allegro_image.h>
%include <allegro5/bitmap.h>
%include <allegro5/bitmap_io.h>
%include <allegro5/altime.h>
%include <allegro5/mouse.h>
%include <allegro5/keyboard.h>
%include <allegro5/timer.h>
%include <allegro5/events.h>
%include <allegro5/keycodes.h>
%include <allegro5/path.h>
%include <allegro5/allegro_primitives.h>
%include <allegro5/transformations.h>

