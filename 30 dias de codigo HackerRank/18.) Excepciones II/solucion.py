class Calculator:
    def power(self,n,m):
        if n < 0 or m < 0:
            raise Exception("n and p should be non-negative")
        return n**m

if __name__ == "__main__":
    myCalculator=Calculator()
    T=int(input())
    for i in range(T):
        n,p = map(int, input().split())
        try:
            ans=myCalculator.power(n,p)
            print(ans)
        except Exception as e:
            print(e)