def main():

    tup1 = (12,"Akshay",31.56,True)
    print(tup1)
    print(tup1[0])
    print(type(tup1))
    print(len(tup1))

    tup2 = (11,65,"Akshay",65)
    for value in tup2:
        print(value)

    for value in range(len(tup2)):
        print(tup1[value])

if __name__ == "__main__":
    main()