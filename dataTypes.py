# Python Example
input_str = input()


for token in input_str.split():
    try:
        # Try to convert to integer
        value = int(token)
    except ValueError:
        try:
            # Try to convert to float
            value = float(token)
        except ValueError:
            # If both conversions fail, keep it as string
            value = token
    
    print(value)

