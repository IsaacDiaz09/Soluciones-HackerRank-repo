# https://www.hackerrank.com/challenges/30-2d-arrays/problem

def findMaxSumHourglasses(array2d):
    lst = []
    for j in range(4):
        for i in range(4):
            sum = 0
            sum += array2d[j][i] + array2d[j][i+1] + array2d[j][i+2]
            sum += array2d[j+1][i+1]
            sum += array2d[j+2][i] + array2d[j+2][i+1] + array2d[j+2][i+2]
            lst.append(sum)
    return max(lst)


if __name__ == "__main__":
    nums = []
    for _ in range(6):
        nums += [[int(i) for i in input().split()]]
    print(findMaxSumHourglasses(nums))
