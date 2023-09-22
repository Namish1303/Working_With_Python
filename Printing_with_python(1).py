#Python allows us some flexibility with printing in different ways 
#printing different strings in different ways
print("-----------1-----------")
print("Hello World")

print("\n-----------2-----------")
x = "Hello"  #defined a variable x with value "Hello"
y= "World"
print(x,y)
#using comma while printing automatically gives space between the 2 variables of either side of the comma while printing


print("\n-----------3-----------")
print(x+y)
#using "+" gives no spacing



print("\n-----------4-----------")
#end
print(x,end="      ")
print(y)
# if you would have noticed each print statement automatically inputs a newline character at the end
# if you want to change the end of line character , you can do it with following steps
