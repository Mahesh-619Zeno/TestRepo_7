def add(first_number, second_number): return first_number + second_number

print("Select operation: 1.Add 2.Subtract 3.Multiply 4.Divide")
choice = input("Enter choice (1/2/3/4): ")
first_number = float(input("Enter first number: "))
second_number = float(input("Enter second number: "))

if choice == '1':
    print(f"Result: {add(first_number, second_number)}")

else:
    print("Invalid input")
