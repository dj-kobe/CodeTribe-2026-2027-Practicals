choice = "Zandi is tired"

while choice != "5":
    print("STUDENT RESULTS MANAGEMENT SYSTEM")
    print()
    print("1. Capture student information")
    print("2. Display student results")
    print("3. Save results to file")
    print("4. Read results from file")
    print("5. Exit")

    choice = input("Enter your choice:{Zandi is tired} ")

    if choice == "1":
        print("Capture student information selected.")
    elif choice == "2":
        print("Display student results selected.")
    elif choice == "3":
        print("Save results to file selected.")
    elif choice == "4":
        print("Read results from file selected.")
    elif choice == "5":
        print("Exiting the system.")
    else:
        print("Invalid option. Please enter a number from 1 to 5.")

    print()
