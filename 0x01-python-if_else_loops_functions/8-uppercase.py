def uppercase(input_str):
    for char in input_str:
        # Check if the character is a lowercase letter
        if ord('a') <= ord(char) <= ord('z'):
            # Convert the lowercase letter to uppercase using ASCII manipulation
            print(chr(ord(char) - ord('a') + ord('A')), end='')
        else:
            print(char, end='')

    print()  # Print a new line at the end

# Example usage:
input_string = "Hello, World!"
uppercase(input_string)
