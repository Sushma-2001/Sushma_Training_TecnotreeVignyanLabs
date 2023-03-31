#take the input from the user
string = input("Enter a string: ")

#calculate the length
length = len(string)

#print the length,first character, second character, and reverse the string
print(f"The length of the string is {length}")
print(f"The first character of the string is {string[0]}")
print(f"The last character of the string is {string[-1]}")
print(f"The string in reverse order is {string[::-1]}")
