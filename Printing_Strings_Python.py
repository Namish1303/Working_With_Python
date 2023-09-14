#Python allows us some flexibility with printing in different ways 
#printing different strings in different ways

print("----- 1 ------")
print("Hello World")


print("\n----- 2 ------")
x ="Hello"
y = "World"
print(x,y)
#using comma while printing automatically gives space between the 2 variables of either side of the comma while printing

print("\n----- 3 ------")
print(x+y)
#using '+' prints the variables as it is without any spaces
print(x+" "+y)


print("\n----- 4 ------")
# if you would have noticed each print statement automatically inputs a newline character at the end
# if you want to change the end of line character , you can do it with following steps

print(x,end=" 'See i changed end of line' ")
print(y)

#you can specify any string in the end section of print to print it at the end