CC        := gcc
LD        := g++
SWIG        := swigwin-2.0.3\swig

SRC_DIR   := src
BUILD_DIR := build

SRC       := $(foreach sdir,$(SRC_DIR),$(wildcard $(sdir)/*.c))
OBJ       := $(patsubst src/%.c,build/%.o,$(SRC))
INCLUDES  := $(addprefix -I,$(SRC_DIR)) -Iallegro-5.0.2-1-mingw-4.5.0\include -Ipython27\include

vpath %.c $(SRC_DIR)

define make-goal
$1/%.o: %.c
	$(CC) $(INCLUDES) -Wall -O2 -DALLEGRO_STATICLINK -c $$< -o $$@
endef

.PHONY: all checkdirs clean

all: checkdirs build/_allegro.pyd examples/python/_allegro.pyd

build/_allegro.pyd: $(OBJ) build/allegro_wrap.o
	$(LD) -shared $^ -o $@ -Lallegro-5.0.2-1-mingw-4.5.0/lib -Lpython27/libs -lpython27 -lallegro-5.0.2-monolith-static-md -lopengl32 -lwinmm -lkernel32 -lpsapi -lgdi32 -lcomdlg32 -lole32 -lgdiplus -luuid -lstrmiids -lfreetype-2.4.4-static-md

build/allegro_wrap.c: src/allegro.i
	$(SWIG) -DALLEGRO_MINGW32 -Iallegro-5.0.2-1-mingw-4.5.0\include -python -o build/allegro_wrap.c src/allegro.i

build/allegro_wrap.o: build/allegro_wrap.c
	$(CC) -Wall -O2 -c -DALLEGRO_STATICLINK $(INCLUDES) -o build/allegro_wrap.o build/allegro_wrap.c

examples/python/_allegro.pyd: build/_allegro.pyd
	copy /Y build\_allegro.pyd examples\python\ && copy /Y build\allegro.py examples\python\
	


checkdirs: $(BUILD_DIR)

$(BUILD_DIR):
	@mkdir $@

clean:
	@erase /F /Q $(BUILD_DIR)

$(foreach bdir,$(BUILD_DIR),$(eval $(call make-goal,$(bdir))))

