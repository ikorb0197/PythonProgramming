# Get the list

n = int(input("Enter the number of elements: "))

elements = []
while n:
    elements.append(int(input()))
    n -= 1

print(elements)

# Check if all the elements are equal
# print true
# otherwise false
if len(elements) < 2:
    print(bool(True))
elif all(elements[i] == elements[i + 1] for i in range(0, len(elements) - 1)): # my work
    print(bool(True)) # my work
else:
    # Finish it at home (FINISHED)
    print(bool(False)) # my work