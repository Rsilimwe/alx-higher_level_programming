def islower(c):
    # Check if the ASCII value of the character is between the ASCII values of 'a' and 'z'
    return ord('a') <= ord(c) <= ord('z')

# Example usage:
char = 'a'
result = islower(char)
print(result)  # Output: True
