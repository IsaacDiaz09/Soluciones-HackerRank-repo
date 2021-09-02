# https://www.hackerrank.com/challenges/30-scope/problem?isFullScreen=true

class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0
    
    def computeDifference(self):
        # Computa el valor absoluto de la resta del menor con el mayor valor el el iterable
        self.maximumDifference = abs(min(self.__elements)-max(self.__elements))


if __name__ =="__main__":
    # Recepcion de datos
    noNeccesaryVar = input()
    a = [int(e) for e in input().split(' ')]
    d = Difference(a)
    d.computeDifference()
    print(d.maximumDifference)
