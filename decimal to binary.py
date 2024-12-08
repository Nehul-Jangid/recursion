def decimalToBinary(x):
    if x == 0:
        return ""
    # Recursive case: process the quotient and add the remainder
    return decimalToBinary(x // 2) + str(x % 2)

# Test the function
print(decimalToBinary(66))  # Output: "1000010"
