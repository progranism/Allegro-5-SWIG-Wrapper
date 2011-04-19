swigwin-2.0.3\swig -DALLEGRO_MINGW32 -Iallegro-5.0.2-1-mingw-4.5.0\include -python allegro.i
gcc -c -DALLEGRO_STATICLINK -I "allegro-5.0.2-1-mingw-4.5.0\include" -Ipython\include allegro_wrap.c allegro.c
g++ -shared allegro_wrap.o allegro.o -o _allegro.pyd -Lallegro-5.0.2-1-mingw-4.5.0\lib -Lpython\libs python\libs\libpython27.a -lallegro-5.0.2-monolith-static-md -lopengl32 -lwinmm -lkernel32 -lpsapi -lgdi32 -lcomdlg32 -lole32 -lgdiplus -luuid -lstrmiids
copy allegro.py examples\python\
copy _allegro.pyd examples\python\
PAUSE
