# https://www.hackerrank.com/challenges/30-interfaces/problem?isFullScreen=true
class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError

class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        sum = 0
        for i in range(1,n+1):
            if n % i == 0:
                sum += i
        return sum


n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
# Le dice que le traiga la clase padre del objeto 'my_calculator', donde se defiinio el metodo a implemetar en la hija
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)
print()
print(type(my_calculator).__bases__)
print(type(my_calculator).__name__)

"""
6

I implemented: AdvancedArithmetic
12

(<class '__main__.AdvancedArithmetic'>,)
Calculator
"""

