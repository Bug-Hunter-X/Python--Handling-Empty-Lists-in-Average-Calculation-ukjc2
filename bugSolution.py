def calculate_average(numbers):
    if not numbers:
        raise ValueError("Cannot calculate the average of an empty list.")
    return sum(numbers) / len(numbers)

# Example usage:
my_numbers = []
try:
    result = calculate_average(my_numbers)
    print(f"The average is: {result}")
except ValueError as e:
    print(f"Error: {e}")

my_numbers = [1, 2, 3, 4, 5]
result = calculate_average(my_numbers)
print(f"The average is: {result}")
