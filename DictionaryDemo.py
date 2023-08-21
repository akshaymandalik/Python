Batches = {"PPA":18500,"LSP":20000} # Key:Value

print(Batches)

print(type(Batches))
print(len(Batches))

print(Batches["LSP"])

for Value in Batches:
    print(Value)

for Value in Batches:
    print(Batches[Value])  

for Value in Batches:
    print(f"{Value}:{Batches[Value]}")