# today we are going to explore more about in methods in class

print ("Ley's start learning")

class goofy:
    def one (self , name): # parameters
        self.name = name
    def two (self):
        return self.name
    def three (self):
        return "Hello %s"  % self.name   # %s is answer of variable
        
c = goofy()  # c is class so will be used in class
d = goofy()
x = goofy()
c.one('waifer')
d.one('kolar')
x.one('shwethwar thanwai')

print (c.two())
print (d.two())
print (c.three())
print (d.three())

print (x.three())

    
