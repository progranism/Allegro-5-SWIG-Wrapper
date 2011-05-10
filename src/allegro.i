%module allegro

%define AL_FUNC(type, name, args)
type name args
%enddef

%{
	#ifdef SWIGMAC
        #include <AppKit/AppKit.h>
	#endif
        #include <allegro5/allegro5.h>
        #include <allegro5/internal/alconfig.h>
	#include <allegro5/allegro_native_dialog.h>
	#include <allegro5/allegro_font.h>
	#include <allegro5/allegro_image.h>
	#include <allegro5/allegro_primitives.h>
	#include <allegro5/allegro_ttf.h>
        #undef al_init
	extern bool al_init();
%}

#ifdef SWIGMAC
extern BOOL NSApplicationLoad(void);
#endif

extern bool al_init();

%ignore al_init;

%include <allegro5/system.h>
%include <allegro5/display.h>
%include <allegro5/color.h>
%include <allegro5/bitmap.h>
%include <allegro5/bitmap_io.h>
%include <allegro5/altime.h>
%include <allegro5/mouse.h>
%include <allegro5/keyboard.h>
%include <allegro5/timer.h>
%include <allegro5/events.h>
%include <allegro5/keycodes.h>
%include <allegro5/path.h>
%include <allegro5/transformations.h>
%include <allegro5/allegro_native_dialog.h>
%include <allegro5/allegro_image.h>
%include <allegro5/allegro_primitives.h>
%include <allegro5/allegro_ttf.h>

// FIXME: allegro_font stuff below
// FIXME: swig doesn't like ALLEGRO_FONT_PRINTFUNC

enum {
   ALLEGRO_ALIGN_LEFT   = 0,
   ALLEGRO_ALIGN_CENTRE = 1,
   ALLEGRO_ALIGN_RIGHT  = 2
};

struct ALLEGRO_USTR;
struct ALLEGRO_FONT;
struct ALLEGRO_FONT_VTABLE;

extern bool al_register_font_loader(const char *ext, ALLEGRO_FONT *(*load)(const char *filename, int size, int flags));
extern ALLEGRO_FONT * al_load_bitmap_font(const char *filename);
extern ALLEGRO_FONT * al_load_font(const char *filename, int size, int flags);
extern ALLEGRO_FONT * al_grab_font_from_bitmap(ALLEGRO_BITMAP *bmp, int n, int ranges[]);
extern void al_draw_ustr(const ALLEGRO_FONT *font, ALLEGRO_COLOR color, float x, float y, int flags, ALLEGRO_USTR const *ustr);
extern void al_draw_text(const ALLEGRO_FONT *font, ALLEGRO_COLOR color, float x, float y, int flags, char const *text);
extern void al_draw_justified_text(const ALLEGRO_FONT *font, ALLEGRO_COLOR color, float x1, float x2, float y, float diff, int flags, char const *text);
extern void al_draw_justified_ustr(const ALLEGRO_FONT *font, ALLEGRO_COLOR color, float x1, float x2, float y, float diff, int flags, ALLEGRO_USTR const *text);
extern void al_draw_textf(const ALLEGRO_FONT *font, ALLEGRO_COLOR color, float x, float y, int flags, char const *format, ...);
extern void al_draw_justified_textf(const ALLEGRO_FONT *font, ALLEGRO_COLOR color, float x1, float x2, float y, float diff, int flags, char const *format, ...);
extern int al_get_text_width(const ALLEGRO_FONT *f, const char *str);
extern int al_get_ustr_width(const ALLEGRO_FONT *f, const ALLEGRO_USTR *ustr);
extern int al_get_font_line_height(const ALLEGRO_FONT *f);
extern int al_get_font_ascent(const ALLEGRO_FONT *f);
extern int al_get_font_descent(const ALLEGRO_FONT *f);
extern void al_destroy_font(ALLEGRO_FONT *f);
extern void al_get_ustr_dimensions(const ALLEGRO_FONT *f,
    ALLEGRO_USTR const *text,
    int *bbx, int *bby, int *bbw, int *bbh);
extern void al_get_text_dimensions(const ALLEGRO_FONT *f,
    char const *text,
    int *bbx, int *bby, int *bbw, int *bbh);
extern void al_init_font_addon(void);
extern void al_shutdown_font_addon(void);
extern uint32_t al_get_allegro_font_version(void);

