# Taking input from the user
num_list = list(map(int, input("Enter a list of numbers: ").split()))

# Sorting the list in ascending order
num_list.sort()

# Finding the length of the list
n = len(num_list)

# Finding the median of the list
if n % 2 == 0:
    median1 = num_list[n//2]
    median2 = num_list[n//2 - 1]
    median = (median1 + median2)/2
else:
    median = num_list[n//2]

# Printing the median value
print("Median of the list is: " + str(median))
