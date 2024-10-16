# Get a positive integer from the user
num = int(input("Enter a positive integer: "))

# Store even numbers less than the integer in a list
even_numbers = [i for i in range(2, num) if i % 2 == 0]

# Print the list of even numbers
print(even_numbers)