name=" khushi nain "
print(name.capitalize())
print(name.upper())
print(name.lower())
print(name.strip())  #remove whitespace from starting and ending
print(name.title())
print(name.swapcase())
print(name.replace("k","K"))
# print(name.centre())
x=name.replace("khushi","sayna")
print(x)
y="khushi nain is soo intelligent"
print(y.split())
z="Khushi#sayna#vansh#geeta"
print(z.split("#"))
print(z.split("#",1))
print(z.find("sayna"))
print(z.find("Khushi"))
print(z.find("vansh"))

txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))