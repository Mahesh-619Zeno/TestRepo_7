x = []
try:
    num_people = int(input("Enter number of people: "))
    for i in range(num_people):
        person_input = input(f"Enter weight(kg) and height(m) for person {i+1}, separated by space: ").split()
        if len(person_input) != 2:
            raise ValueError("Two values required")
        x.append(tuple(map(float, person_input)))
except ValueError as e:
    print("Invalid input:", e)
    exit()

print("\n--- BMI Report ---")
for idx, data in enumerate(x, 1):
    bmi = data[0] / (data[1] ** 2) if data[1] > 0 else 0.0
    status = "Underweight" if bmi < 18.5 else "Normal" if bmi < 25 else "Overweight" if bmi < 30 else "Obese"
    print(f"Person {idx}: Weight = {data[0]} kg, Height = {data[1]} m, BMI = {bmi:.2f}, Status = {status}")
