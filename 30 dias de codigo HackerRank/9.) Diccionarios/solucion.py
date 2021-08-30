# https://www.hackerrank.com/challenges/30-dictionaries-and-maps/problem

def phoneNumbers(n):
    dict = {}
    for _ in range(n):
        nameAndPhone = [i for i in input().split()]
        dict[nameAndPhone[0]] = nameAndPhone[1]
    
    while True:
        try:
            query = input()
            if query in dict:
                print(f"{query}={dict.get(query)}")
            else:
                print("Not found")
        except:
            break

