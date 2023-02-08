print("Enter the number of seats")
seats = int(input(">>> "))

print("Enter how many people are sitting in bus")
sit = int(input(">>> "))

print("Enter how many people got off at the stop")
people = int(input(">>> "))

print("Enter how many people want to enter the bus")
want_people = int(input(">>> "))

space = seats - (sit - people)

if want_people < 0:
    print("You're joking")
elif seats < 0:
    print("You're joking")
elif sit < 0:
    print("You're joking")
elif people < 0:
    print("You're joking")
elif space >= want_people:
    print("Welcome to the bus!")
elif space < want_people:
    print("Sorry, but we don't have enough space.")