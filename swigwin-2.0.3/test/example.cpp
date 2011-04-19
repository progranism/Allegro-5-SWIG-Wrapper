#include "example.h"

MyClass *last_class = 0;

void consume(MyClass *obj)
{
	last_class = obj;
}

MyClass *eject()
{
	return last_class;
}

