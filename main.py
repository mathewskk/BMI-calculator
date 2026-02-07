FILE_NAME = "bmi_records.txt"


def calculate_bmi(weight, height):
    return weight / (height ** 2)


def get_health_status(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"


def save_record(name, weight, height, bmi, status):
    with open(FILE_NAME, "a") as file:
        file.write(f"{name} | {weight} | {height} | {bmi:.2f} | {status}\n")


def view_records():
    try:
        with open(FILE_NAME, "r") as file:
            records = file.readlines()
            if not records:
                print("No records found.")
            else:
                print("\n--- Saved BMI Records ---")
                for record in records:
                    print(record.strip())
    except FileNotFoundError:
        print("No records file found. Please add a record first.")


while True:
    print("\n===== BMI CALCULATOR MENU =====")
    print("1. Calculate BMI and Save")
    print("2. View All BMI Records")
    print("3. View BMI Categories")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        try:
            name = input("Enter name: ")
            weight = float(input("Enter weight (kg): "))
            height = float(input("Enter height (m): "))

            if weight <= 0 or height <= 0:
                print("Weight and height must be positive.")
            else:
                bmi = calculate_bmi(weight, height)
                status = get_health_status(bmi)

                print(f"\n{name}'s BMI: {bmi:.2f}")
                print("Health Status:", status)

                save_record(name, weight, height, bmi, status)
                print("Record saved successfully ✅")

        except ValueError:
            print("Invalid input! Please enter numbers only.")

    elif choice == "2":
        view_records()

    elif choice == "3":
        print("\n--- BMI Categories ---")
        print("Below 18.5  : Underweight")
        print("18.5 - 24.9 : Normal")
        print("25 - 29.9   : Overweight")
        print("30 and above: Obese")

    elif choice == "4":
        print("Exiting BMI Calculator. Goodbye! 👋")
        break

    else:
        print("Invalid choice. Please try again.")
