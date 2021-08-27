# https://www.hackerrank.com/challenges/30-operators/

def mealTotalCost(base,tip,tax):
    totalCost = base + (base*(tip/100)) + (base*(tax/100))
    # halla el valor total calculando a cuanto equivale cada % y entrega la respuesta en un entero redondeado
    return int(round(totalCost))

if __name__ == "__main__":
    # precio base de la comida
    mealBasePrice = float(input())
    # % de propina
    tipPercent = int(input())
    # % de impuesto
    taxPercent = int(input())

    print(mealTotalCost(mealBasePrice,tipPercent,taxPercent))
