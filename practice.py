# user inputs - bill amount, tip percentage, number of people splitting the bill and include service charge

bill_amount = int(input("What was the bill? "))
tip_percentage = int(input("What % tip would you like to give? "))
num_people = int(input("How many people are splitting the bill? "))
include_service_charge = input("Include a service charge? (yes/no): ")
service_charge = 100

# function

def tip_calculator():
    tip = (bill_amount * tip_percentage) /100
    total_amount = bill_amount + tip

    if include_service_charge == 'yes':
        total_amount += service_charge

    pay_per_person = total_amount / num_people

    print(f"\nEach person should pay: KES {pay_per_person:.2f}")

tip_calculator()