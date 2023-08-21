def main():

    Batch_Name = ["PPA","LB","Python Programming","LSP"]
    Fees = [18500,15600,18500,20000]

    for iCnt in range(len(Fees)):
        print(f"{Batch_Name[iCnt]}:{Fees[iCnt]}")
    
if __name__ == "__main__":
    main()