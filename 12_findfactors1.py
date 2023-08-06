def findfactors(iNo):

    condition = range(1, (int(iNo/2)+1))
    iCnt = 1
    while (iCnt <= iNo/2):
        if iNo % iCnt == 0:
            print(iCnt)
        iCnt+=1    

def main():
    
    iNo = 0
    iNo = int(input("Enter Number:"))
    findfactors(iNo)

if __name__ == "__main__":
    main()