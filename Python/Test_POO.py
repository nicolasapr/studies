#testing class

class dog:
    def __init__(self, name, age, hungry, live, timeWF):
        self.name = name
        self.age = age
        self.hungry = False
        self.live = True
        self.timeWF = 0
    def eat(self):
        self.hungry = False
        self.timeWF = 0
        print(self.name + " is eating")
    def bark(self):
        print(self.name + " is barking")
    def info(self):
        print(f"{self.name} is {self.age} years old and its hungry status is {self.hungry}")
    def older(self):
        self.age += 1
        self.timeWF += 1

        print(f"{self.name} is now {self.age} years old")
    def timeWithoutFood(self):
        if self.timeWF >= 3:
            self.live = False
            print(f"{self.name} is dead")
    