# https://www.hackerrank.com/challenges/30-review-loop/problem

def separateStringByEvenOddIndex(n):
    for _ in range(n):
        firstStr = ""
        secondStr = ""
        str = input()
        for i in range(0,len(str)):
            if i % 2 == 0:
                firstStr += str[i]
            else:
                secondStr += str[i]
        print(f"{firstStr} {secondStr}")


if __name__ == "__main__":
    n = int(input())
    separateStringByEvenOddIndex(n)
