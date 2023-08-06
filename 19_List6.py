def main():
    print("Enter No. of Elements that you want to store:")
    length = int(input())

    Arr = list()

    print("Enter Elements:")

    for i in range(0,length):
        value = (input())
        Arr.append(value)

    print("Elements of Arr are:")
    for i in range(0,length):
        print(Arr[i])
        print(type(Arr[i]))

if __name__ == "__main__":
    main()