# https://www.hackerrank.com/challenges/saying-hi/problem?isFullScreen=false
import re

if __name__ == "__main__":
    for _ in range(int(input())):
        s = input()
        if re.match(r"^[H|h][I|i] [^Dd]", s):
            print(s)
