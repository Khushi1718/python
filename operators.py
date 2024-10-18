# Python divides the operators in the following groups:

# Arithmetic operators
# Assignment operators
# Comparison operators
# Logical operatorsppp
# Identity operators
# Membership operators
# Bitwise operators
x=10
y=5
#Arithmetic operator

print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x//y)   #floor division
print(x**y)
print(x%y)   #modulus

################################################################


#Assignment operator
# 	x = 5	
# +=	x += 3	    x = x + 3	
# -=	x -= 3	    x = x - 3	
# *=	x *= 3	    x = x * 3	
# /=	x /= 3	    x = x / 3	
# %=	x %= 3	    x = x % 3	
# //=	x //= 3	    x = x // 3	
# **=	x **= 3	    x = x ** 3	
# &=	x &= 3	    x = x & 3	
# |=	x |= 3   	x = x | 3	
# ^=	x ^= 3	    x = x ^ 3	
# >>=	x >>= 3 	x = x >> 3	
# <<=	x <<= 3  	x = x << 3	
# :=	print(x := 3)	x = 3
# print(x)


###################################################33


#python comparision operator
# x==y
# x!=y
# x>y
# x<y
# x>=y
# x<=y


#######################################################################


#Logical Operator(and or not)

x = 5

print(not(x > 3 and x < 10))

# returns False because not is used to reverse the result

####################################################################

# Identity operator
# is 	      (Returns True if both variables are the same object)	x is y	
# is not	  (Returns True if both variables are not the same object)	x is not y
x=5
y=5
print(x is not y)
print(x is y)


##################################################################################33


#Membership operator
# in 	     (Returns True if a sequence with the specified value is present in the object)	x in y	
# not in	(Returns True if a sequence with the specified value is not present in the object)	x not in y

x = ["apple", "banana"]

print("banana" in x)
print("khushi" in x)

# returns True because a sequence with the value "banana" is in the list


#################################################################################3


#Bitwise Operator

# & 	(AND	Sets each bit to 1 if both bits are 1)	        x & y	
# |	     (OR	Sets each bit to 1 if one of two bits is 1)   	x | y	
# ^	      (XOR	Sets each bit to 1 if only one of two bits is 1)	x ^ y	
# ~	     (NOT	Inverts all the bits)	                            ~x	
# <<	(Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off)	x << 2	
# >>	(Signed right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off)	x >> 2	
 
print(6&3)
print(6|3)
print(6^3)
print(~3)


