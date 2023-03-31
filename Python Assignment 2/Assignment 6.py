# Take input from user for the list of words
word_list = input("Enter a list of words: ")

# Split the input string into a list of words
word_list = word_list.split()

# Initialize a variable to store the longest word
longest_word = ""

# Iterate over each word in the list
for word in word_list:
    
    # If the length of the current word is greater than the length of the longest word so far
    if len(word) > len(longest_word):
        
        # Update the longest word variable
        longest_word = word

# Print the longest word
print("The longest word in the list is:", longest_word)
