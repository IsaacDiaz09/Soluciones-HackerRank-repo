# https://www.hackerrank.com/challenges/30-inheritance/problem

class Person:
    def __init__(self, firstName, lastName, id):
        self.firstName = firstName
        self.lastName = lastName
        self.id = id

    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.id)


class Student(Person):
    def __init__(self, firstName, lastName, id,*scores):
        super().__init__(firstName,lastName,id)
        self.scores = scores
    """
    Llamar al metodo super para sobre escribir el metodo init y pasar el nuevo parametro de la clase hija --> (scores)
    """
    def calculate(self):
        sum = 0
        for i in self.scores:
            sum += i
        average = sum/len(self.scores)

        if average >= 90 and average <= 100:
            return "Grade: O"
        elif average >= 80 and average < 90:
            return "Grade: E"
        elif average >= 70 and average < 80:
            return "Grade: A"
        elif average >= 55 and average < 70:
            return "Grade: P"
        elif average >=40 and average <55:
            return "GRADE D"
        elif average < 40:
            return "Grade: T"


if __name__ == "__main__":
    nameAndId = [i for i in input().split()]
    uselessVar = input() #No necesaria en python para hallar el promedio
    grades = tuple([int(j) for j in input().split()])
    s = Student(nameAndId[0],nameAndId[1],nameAndId[2],*grades)
    s.printPerson()
    print(s.calculate())
