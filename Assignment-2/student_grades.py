import json

FILE_NAME = "students.json"

# Load data from file
def load_data():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except:
        return {}

# Save data to file
def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)

students = load_data()

while True:
    print("\n1. Add Student")
    print("2. Update Grade")
    print("3. Display Students")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        grade = input("Enter grade: ")
        students[name] = grade
        save_data(students)
        print("✅ Student added and saved!")

    elif choice == "2":
        name = input("Enter name: ")
        if name in students:
            grade = input("Enter new grade: ")
            students[name] = grade
            save_data(students)
            print("✅ Updated successfully!")
        else:
            print("❌ Student not found")

    elif choice == "3":
        if students:
            print("\n📊 Student Grades:")
            for name, grade in students.items():
                print(name, ":", grade)
        else:
            print("⚠️ No data found")

    elif choice == "4":
        print("Exiting...")
        break

    else:
        print("Invalid choice")