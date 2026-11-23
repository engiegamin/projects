print("Change calculator")
amount_due = float(input("Enter the amount due: "))
amount_received = float(input("Enter the amount received: "))
change = amount_received - amount_due
print(f"Change to be given: ${change:.2f}")