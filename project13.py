r = int(input("Enter the radius: "))

circumference = 2 * 3.14 * r
if r < 0:
    print("The radius cannot be negative.")
else:
    print(f"The circumference of the circle is: {circumference}")