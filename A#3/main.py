class Parrot:
    #class attribute
    species="bird"
    #Instance attribute
    def __init__(self,name,age):
       self.name= name
       self.age= age
b=Parrot("Blue",10)
w=Parrot("Woo",15)
print("Blue is a {}".format(b.species))
print("Woo is also a {}".format(w.species))
print("{} is {} years old".format( b.name, b.age))
print("{} is {} years old".format( w.name, w.age))



    