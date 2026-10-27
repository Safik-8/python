class Student:
    def __init__(self, name, age, rollNo):
        self.name= name
        self.age= age
        self.rollNo= rollNo

    def display(self):
        print(self.name, self.age, self.rollNo)


s1= Student("Safik", 22, 67)
s2= Student("dwjch", 22, 67)


s1.display()
s2.display()