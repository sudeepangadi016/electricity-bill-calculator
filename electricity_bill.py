def validate_input(units):
    """
    Validate if input is valid (positive number).
    Returns True if valid, False otherwise.
    """
    try:
        value = float(units)
        
        # Check for negative values
        if value < 0:
            print("Error: Units cannot be negative!")
            return False
        
        # Check for zero value
        if value == 0:
            print("Error: Units cannot be zero!")
            return False
        
        return True
    
    except ValueError:
        # Character or invalid input
        print("Error: Invalid input! Please enter a valid numeric value.")
        return False
    except TypeError:
        print("Error: Input type is not supported!")
        return False


def calculate_bill(units):
    """Calculate electricity bill based on units consumed."""
    slabs = [
        (50, 3.0),
        (100, 4.5),
        (200, 6.0),
        (float("inf"), 8.0)
    ]
    
    total = 0.0
    remaining = units
    
    for limit, rate in slabs:
        if remaining <= 0:
            break
        used = min(remaining, limit)
        total += used * rate
        remaining -= used
    
    return total


# Main program
if __name__ == "__main__":
    print("=" * 40)
    print("ELECTRICITY BILL CALCULATOR")
    print("=" * 40)
    
    while True:
        units_input = input("\nEnter units consumed (or 'quit' to exit): ")
        
        if units_input.lower() == 'quit':
            print("Thank you for using the calculator!")
            break
        
        if validate_input(units_input):
            units = float(units_input)
            bill = calculate_bill(units)
            
            print(f"\n{'-' * 40}")
            print(f"Units Consumed: {units} kWh")
            print(f"Total Bill: Rs. {bill:.2f}")
            print(f"{'-' * 40}\n")
        else:
            print("Please try again with a valid input.\n")
