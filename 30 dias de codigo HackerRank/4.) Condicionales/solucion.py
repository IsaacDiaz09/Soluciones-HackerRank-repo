# https://www.hackerrank.com/challenges/30-conditional-statements/problem

# Comprueba si es impar o no
def isEven(n):
    if n % 2 == 0:
        return True
    return False


# Funcion que comprueba las condiciones
def isWeird(n):
    if isEven(n) and 2<=n<=5:
        return "Not Weird"
    elif isEven(n) and 6<=n<=20:
        return "Weird"
    elif isEven(n) and n>20:
        return "Not Weird"
    elif isEven(n) is False:
        return "Weird"

if __name__ == "__main__":
    # Se solicita el numero y se muestra el resultado
    number = int(input())
    print(isWeird(number))
