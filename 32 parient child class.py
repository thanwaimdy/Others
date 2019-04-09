# you will learn more about superclass and subclass

print("Hello let's start the class")

class parents:
    var1 = "one"
    var2 = "two"
    
class child(parents):
#    var1 = "one"
#    var2 = "two" 
    
    var2 = "three"



    
obj = parents()
cobj = child()

print(obj.var1)
print(obj.var2)
print(cobj.var1)
print(cobj.var2)

 

