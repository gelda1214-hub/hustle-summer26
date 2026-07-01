# Dagim Gedle / lab 4 / Intro to python

# Ticket 1 
ages = [17, 11, 25, 13, 9]
# Predict = Access granted = 17, 25, 13 Too young = 9, 11

for age in ages:
    if age >= 13:
        print(age, "- Access allowed")
    else:
        print(age, "- Access denied")
        # Explain = It holds the ages in one varaible

        # Ticket 1
        # Predict = no
    again = "yes"

while again == "yes":
    age = int(input("Enter an age: "))

    if age >= 13:
        print("Access allowed")
    else:
        print("Access denied")

    again = input("Do you want to check another age?")
    # Explain = Because while loops are kinda for true or false

    # Ticket 1 
    # Predict + the loop wouldnt end
    while True:
     age = input("Enter an age")

     if age.lower() == "stop":
        print("Goodbye!")
        break

    age = int(age)

    if age >= 13:
        print("Access granted.")
    else:
        print("Access denied")

        #Ticket 1 
        # Predict = It uses def
        def can_access(age):
         if age >= 13:
          while True:
         else:
            while False:

             ages = [10, 13, 15, 8, 20]
             # Explain = for clarity

for age in ages:
    if can_access(age):
        print(f"Age {age}: Access granted.")
    else:
        print(f"Age {age}: Access denied.")
        #ticket 1 
        signup_report(ages):
    approved = 0

    for signup_number, age in enumerate(ages, start=1):
        if age >= 13:
            print("Signup {signup_number}: Age {age} - Approved")
            approved += 1
        else:
            print("Signup {signup_number}: Age {age} - Denied")

    print(f"\nApproved: {approved} out of {len(ages)}")


signups = [22, 10, 15, 8, 19, 13]
signup_report(signups)