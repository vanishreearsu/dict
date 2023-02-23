# create an empty dictionary
ascii_dict = {}

# loop through the alphabets a to z and add key-value pairs to the dictionary
for char in range(ord('a'), ord('z')+1):
    ascii_dict[chr(char)] = char
    
# print the dictionary
print(ascii_dict)
