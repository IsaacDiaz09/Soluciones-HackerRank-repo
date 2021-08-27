class Person():

    def __init__(self,initialAge):
        if initialAge>=0:
            self.age = initialAge
        else:
            self.age = 0
            print("Age is not valid, setting age to 0.")
    
    def yearPasses(self):
        self.age += 1
    
    def amIOld(self):
        if self.age < 13:
            print("You are young.")
        elif self.age>=13 and self.age<18:
            print("Yor are a teenager.")
        else:
            print("Yor are old.")
 
if __name__ == "__main__":
    n = int(input())
    for _ in range(0,n):
        age = int(input())
        person = Person(age)
        person.amIOld()
        for _ in range(0,3):
            person.yearPasses()
        person.amIOld()
    print()