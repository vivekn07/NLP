def FA(s):
    # If the length is less than 3, then it can't be accepted. Therefore, end the process.
    if len(s) < 3:
        return "Rejected"

    # Check if the first character is '1'
    if s[0] == '1':
        # Check if the second character is '0'
        if s[1] == '0':
            # Check if the third character is '1'
            if s[2] == '1':
                # Check if all remaining characters are '1'
                for i in range(3, len(s)):
                    if s[i] != '1':
                        return "Rejected"
                return "Accepted"  # If all conditions are true
            return "Rejected"  # Else of the third if
        return "Rejected"  # Else of the second if
    return "Rejected"  # Else of the first if


# List of input strings to test the function
inputs = ['1', '10101', '101', '10111', '01010', '100', '', '10111101', '1011111']

# Test the function with each input and print the result
for i in inputs:
    print(FA(i))
