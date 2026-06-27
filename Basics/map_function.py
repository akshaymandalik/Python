def square_of(x):
    return x*x

numbers = [1,2,3,4,5]
squares = map(square_of,numbers)
print(list(squares))