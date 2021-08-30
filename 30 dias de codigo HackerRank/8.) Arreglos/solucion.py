# https://www.hackerrank.com/challenges/30-arrays/problem
import numpy as np

def reversedArrays(listNumbers):
    array = np.array(listNumbers[::-1])
    for n in array:
        print(n,end=" ")


if __name__ == "__main__":
    n = int(input())
    nums = [int(i) for i in input().split()]
    reversedArrays(nums)
