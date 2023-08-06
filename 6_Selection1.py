def main():
    print("Enter A Number:")
    iVal = int(input())
    if iVal%2 == 0:
        print(f"{iVal} is Even")
    else:
        print(f"{iVal} is Odd")    

if __name__ == "__main__":
    main()