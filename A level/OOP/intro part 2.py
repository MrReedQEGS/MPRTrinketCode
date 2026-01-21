#Create a new class that we can use to make people...this time it has some functionality too
class MyPerson:
    def __init__(self, name, age, town):
        self.name = name
        self.age = age
        self.town = town
        
    def PrintAllDetails(self):
        print("Hello my name is " + self.name + " and I am " + str(self.age) + " years old and I live in a town called " + self.town + ".")
        
#MAIN BODY
#Now let's make some people!

people = []
people.append(MyPerson("Fred",3,"Wakefield"))
people.append(MyPerson("Jim",5,"Huddersfield"))
people.append(MyPerson("Bob",19,"Leeds"))
people.append(MyPerson("Simon",56,"Dewsbury"))

#Let's interact with the people...

for person in people:
   person.PrintAllDetails()
   print("")
