# https://www.hackerrank.com/challenges/30-sorting/problem

def bubbleSort(arr):
    numberOfSwaps = 0
    for _ in range(len(arr)):
        for k in range(len(arr)-1):
            if arr[k] > arr[k+1]:
                temp = arr[k]
                arr[k] = arr[k+1]
                arr[k+1] = temp
                numberOfSwaps += 1
        
        if numberOfSwaps == 0:
            break
    
    print("Array is sorted in {} swaps.".format(numberOfSwaps))
    print("First Element: {}".format(arr[0]))
    print("Last Element: {}".format(arr[-1]))

if __name__ == "__main__":
    n = int(input())
    a = [int(i) for i in input().split()]
    bubbleSort(a)
