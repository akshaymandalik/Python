def checkEven(iVal):

    if iVal%2 == 0:
        print(f"{iVal} is Even")
    else:
        print(f"{iVal} is Odd") 

def main():
    print("Enter A Number:")
    iVal = int(input())
    checkEven(iVal)

if __name__ == "__main__":
    main()