# Display welcome message
print("Welcome to Maria Eduarda Gonçalves's System!")

# Get user input for base rate and client's age
base_rate = float(input("Enter the plan's base rate: $ "))
age = int(input("Enter the client's age: "))

# Validate age and calculate the monthly fee based on age brackets
if age < 0:
    print("Invalid age.")
else:
    if age < 19:
        monthly_fee = base_rate
    elif age < 29:
        monthly_fee = base_rate * 1.5
    elif age < 39:
        monthly_fee = base_rate * 2.25
    elif age < 49:
        monthly_fee = base_rate * 2.4
    elif age < 59:
        monthly_fee = base_rate * 3.5
    else:
        monthly_fee = base_rate * 6

    # Display the final calculated monthly fee
    print(f"The monthly plan fee is: $ {monthly_fee:.2f}")