def Add(iNum,iNum1):

    return iNum + iNum
     

def main():

    iVal1 = int(input("Enter First Number:"))
    iVal2 = int(input("Enter Second Number:"))
    iRet = 0

    iRet = Add(iVal1,iVal2)
    print(f"The Addition is {iRet}")

if __name__ == "__main__":
    main()  