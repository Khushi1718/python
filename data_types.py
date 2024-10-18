# Text Type:	str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview
# None Type:	NoneType

# x = "Hello World"	     str	
# x = 20	             int	
# x = 20.5	             float	
# x = 1j	             complex	
# x = ["apple", "banana", "cherry"]	   list	
# x = ("apple", "banana", "cherry")	   tuple	
# x = range(6)	                       range	
# x = {"name" : "John", "age" : 36}	   dict	
# x = {"apple", "banana", "cherry"}   	set	
# x = frozenset({"apple", "banana", "cherry"})	frozenset	
# x = True	                                    bool	
# x = b"Hello"                               	bytes	
# x = bytearray(5)	                            bytearray	
# x = memoryview(bytes(5))	                    memoryview	
# x = None	                                    NoneType
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

x = str("Hello World")
print(x)	
x = int(20)	
print(x)	
x = float(20.5)	
print(x)	
x = complex(1j)	
print(x)	
x = list(("apple", "banana", "cherry"))	
print(x)	
x = tuple(("apple", "banana", "cherry"))	
print(x)
x = range(6)	
print(x)	
x = dict(name="John", age=36)
print(x)	
x = set(("apple", "banana", "cherry"))
print(x)	
x = frozenset(("apple", "banana", "cherry"))	
print(x)
x = bool(5)	
print(x)	
x = bytes(5)
print(x)		
x = bytearray(5)
print(x)