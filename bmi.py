
people_data = [tuple(map(float, input(f"Enter weight(kg) and height(m) for person {i+1}), separated by space: ").split())) for i in range(int(input("Enter number of people: ")))]

print("\n--- BMI Report ---")
for idx, data in enumerate(people_data, 1):
    bmi = data[0] / (data[1] ** 2)
    status = "Underweight" if bmi < 18.5 else "Normal" if bmi < 25 else "Overweight" if bmi < 30 else "Obese"
    print(f"Person {idx}: Weight = {data[0]} kg, Height = {data[1]} m, BMI = {bmi:.2f}, Status = {status}")
