# Create a lambda function
add = lambda x, y: x + y
# Implement subtraction, multiplication, and division
# Check the division by zero
subtract = lambda x, y: x - y
multiply = lambda x, y: x * y
divide = lambda x, y: x / y if y != 0 else "Error: Division by zero!"

# Test the function
# Create a list of tuples
inputs = [(10, 5), (8, 0), (14, 6)]
for x, y in inputs:
    print(f"Inputs: {x}, {y}")
    print(f"Addition: {add(x, y)}")
    print(f"Subtraction: {subtract(x, y)}")
    print(f"Multiplication: {multiply(x, y)}")
    print(f"Division: {divide(x, y)}")