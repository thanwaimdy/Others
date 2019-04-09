# Hello we are going to explore OOP in python.
# Waifer Kolar 

class waifer:         #class
    name = 'waifer'   #attribute
    age = 28          #  =
    def method1 (self):   # here (self) what? don't know.
        return "hey i am method one"   # why used the return?
    def method2 (self):
        return "hey i am method two"
 
    def method3 (self , x):
        self.name = x
        return x    # here if ommit the return
                    # will be show None in the answer
        
                
kolar = waifer()    # object here
print (kolar.name)
print (kolar.age)
print (kolar.method1())
print (kolar.method2())

print (kolar.method3('\nmethod three'))
# hete ('method three') is replace (passing trough) at x
print (kolar.name)