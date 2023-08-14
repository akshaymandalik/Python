def chkNum(iNum):

    if(iNum %2 == 0):
        print("Even Number")
    else:
         print("Odd Number")   

def main():

    iVal = int(input("Enter Number:"))

    chkNum(iVal)

if __name__ == "__main__":
    main()    