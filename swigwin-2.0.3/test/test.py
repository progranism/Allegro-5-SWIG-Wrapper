import Example

a = Example.MyClass()
a.bar = "Puppies"

Example.consume(a)
b = Example.eject()

## Should output "Puppies"
print b.bar

