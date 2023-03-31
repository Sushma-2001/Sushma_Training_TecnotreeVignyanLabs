a = input("Enter a list of numbers").split()
a = [int(num) for num in a]

even_sum = 0
for num in a:
    if num % 2 == 0:
        even_sum += num

print("Sum of all the even numbers:", even_sum)
