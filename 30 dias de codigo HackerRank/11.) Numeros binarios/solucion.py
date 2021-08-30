# https://www.hackerrank.com/challenges/30-binary-numbers/problem

# Se halla la representacion en binario de un numero introducido por teclado 
# y se halla la mayor cantidad de 1 consecutivos que este tiene

def toBinary(num):
    cociente = 2
    resultado = ""
    while cociente > 0:
        cociente = num // 2
        resto = num % 2
        resultado += str(resto)
        num = cociente
    return resultado[::-1]


def consecutiveOnesInBinaryNumber(n):
    lst = []
    numberOfOnes = 0
    for i in toBinary(n):
        if i == "1":
            numberOfOnes += 1
        else:
            numberOfOnes = 0
        lst.append(numberOfOnes)
    return max(lst)


if __name__ == "__main__":
    num = int(input())
    print(consecutiveOnesInBinaryNumber(num))
