numbers = input("Enter a list of numbers, separated by spaces: ").split()

numbers = [int(num) for num in numbers]

largest = max(numbers)
smallest = min(numbers)

print(f"The largest number in the list is {largest}")
print(f"The smallest number in the list is {smallest}")
