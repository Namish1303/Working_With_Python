x = 5
y = 10.0
#we can defined variables as float by adding the decimal place (example y= 2.4)

print(x)
print(y)
print(x+y)
print(x,y)


print("__________Printing ints and floats with strings _______________")
#print("x="+x)
#only strings can be appended at the end of another string while printing
#uncommenting line 13 will give you an error because it tries to append int after a string
#there are 2 ways to do it

#either
print("x:",x)
#or
print("x:"+str(x))
#here we converted x into a string type and appended it to the other string 
#NOTE :- Notice the space difference in both the prints
#same can be done for float type

print("y:",y)
print("y:"+str(y))