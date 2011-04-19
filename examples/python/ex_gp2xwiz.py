from allegro import *
import random
import math

W = 320
H = 240
R = 240
POINTS = 200


al_init()
al_init_primitives_addon()

d = al_create_display(W, H)

v = []
for i in range(0, POINTS):
	v.append(ALLEGRO_VERTEX())

c = ALLEGRO_COLOR()

v[0].x = 0
v[0].y = 0
c = al_map_rgb(random.randrange(0, 256), random.randrange(0, 256), random.randrange(0, 256))
v[0].color = c
v[1].x = 0+R
v[1].y = 0
c = al_map_rgb(random.randrange(0, 256), random.randrange(0, 256), random.randrange(0, 256))
v[1].color = c

a = 0.0
r = R

for i in range(2, POINTS):
	v[i].x = math.cos(a)*r
	v[i].y = math.sin(a)*r
	a += 0.3
	r -= 1.5
	c = al_map_rgb(random.randrange(0, 256), random.randrange(0, 256), random.randrange(0, 256))
	v[i].color = c

frames = 0

t = ALLEGRO_TRANSFORM()

while True:
	al_clear_to_color(al_map_rgb(0, 0, 0))
	al_identity_transform(t)
	al_rotate_transform(t, frames*0.1)
	al_translate_transform(t, W/2, H/2)
	al_use_transform(t)
	al_draw_prim(v, None, None, 0, POINTS, ALLEGRO_PRIM_TRIANGLE_FAN)
	al_flip_display()
	frames += 1
	if frames > 400:
		break

al_uninstall_system()


