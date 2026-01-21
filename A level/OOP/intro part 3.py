#Create a new class that we can use to make people...this time it has some functionality too
class MyPerson:
  
    #static variables
    numOfPeople = 0
  
    def __init__(self, name, age, town):
        self.name = name
        self.age = age
        self.town = town
        
        #Update the static variable each time a new person object is created.
        MyPerson.numOfPeople = MyPerson.numOfPeople + 1
        
    def PrintAllDetails(self):
        print("Hello my name is " + self.name + " and I am " + str(self.age) + " years old and I live in a town called " + self.town + ".")
        
    def __add__(self, otherPerson):
        return (self.age + otherPerson.age)
        

#MAIN BODY
#Now let's make some people!
person1 = MyPerson("Fred",3,"Wakefield")
person2 = MyPerson("Jim",5,"Huddersfield")
person3 = MyPerson("Simon",20,"Leeds")

#Let's interact with the people to find their total age.
ans = person1 + person2

#You cant do function overloading in python so the 3rd person must be added maually.
ans = ans + person3.age
print(ans)

#Print out how many people objects we have
print(MyPerson.numOfPeople)
