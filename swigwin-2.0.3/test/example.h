class MyClass
{
public:
	int foo;
};

// Black box functions.
// Only thing guaranteed is that the last object handed to consume
// will be returned by eject.
void consume(MyClass *obj);
MyClass *eject();

