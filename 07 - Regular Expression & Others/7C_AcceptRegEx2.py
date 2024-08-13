def FA(s):
    size = 0
    # Scan the complete string and make sure that it contains only 'a' & 'b'
    for i in s:
        if i == 'a' or i == 'b':
            size += 1
        else:
            return "Rejected"

    # After checking that it contains only 'a' & 'b'
    # Check its length; it should be at least 3
    if size >= 3:
        # Check the last 3 elements
        if s[size - 3] == 'b':
            if s[size - 2] == 'b':
                if s[size - 1] == 'a':
                    return "Accepted"  # If all 4 if conditions are true
                return "Rejected"  # Else of the 4th if
            return "Rejected"  # Else of the 3rd if
        return "Rejected"  # Else of the 2nd if
    return "Rejected"  # Else of the 1st if


# List of input strings to test the function
inputs = ['bba', 'ababbba', 'abba', 'abb', 'baba', 'bbb', '']

# Test the function with each input and print the result
for i in inputs:
    print(FA(i))
