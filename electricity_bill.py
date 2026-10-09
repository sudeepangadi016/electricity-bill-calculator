def calculate_bill(units):
    """Calculate electricity bill based on units consumed."""
    if units <= 0:
        return 0
    
    # Define slabs and rates
    slabs = [(100, 5), (200, 7), (300, 10), (float('inf'), 12)]
    
    bill = 0
    prev_limit = 0
    
    for limit, rate in slabs:
        if units > prev_limit:
            consumed = min(units, limit) - prev_limit
            bill += consumed * rate
            prev_limit = limit
        else:
            break
    
    return bill

# Main program
if __name__ == "__main__":
    try:
        units = float(input("Enter units consumed: "))
        bill = calculate_bill(units)
        print(f"\n{'=' * 30}")
        print(f"Units Consumed: {units} kWh")
        print(f"Total Bill: Rs. {bill:.2f}")
        print(f"{'=' * 30}\n")
    except ValueError:
        print("Invalid input! Please enter a valid number.")
