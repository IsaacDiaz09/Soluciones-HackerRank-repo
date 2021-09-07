if __name__ == "__main__":
    S = input()
    try:
        n = int(S)
        print(n)
    except ValueError:
        print("Bad String")
