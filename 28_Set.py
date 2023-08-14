def main():

    set1 = {11,11,34.54,"Akshay"}
    search_key = int(input("Enter Value that you want to search:"))
    ret = False

    for value in set1:
        if(value == search_key):
            ret = True
            break
    
    if (ret == True):
        print("Element Found\n")
    else:
        print("No Element\n")

if __name__=="__main__":
    main()