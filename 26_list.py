def main():

    mylist = ["Akshay","Mandalik",12,12.90]
    print(mylist)
    print(mylist[0])

    list1 = [1,1,1,4,5,6]
    print(list1)
    list1[0] = 23
    print(list1)

    list1.append(101)
    print(list1)

    list1.remove(1)  # Which element to remove is needed?
    print(list1)

if __name__ == "__main__":
    main()    