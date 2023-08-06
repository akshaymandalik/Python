def findfactors(iNo):

    condition = range(1, (int(iNo/2)+1))
    for iCnt in condition:
        if iNo % iCnt == 0:
            print(iCnt)

def main():
    
    iNo = 0
    iNo = int(input("Enter Number:"))
    findfactors(iNo)

if __name__ == "__main__":
    main()