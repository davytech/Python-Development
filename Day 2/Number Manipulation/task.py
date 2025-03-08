print("Welcome to Burgeon tip calculator...")
bill = float(input("What was the total bill?\n$"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15?\n"))
people = int(input("How many people will split the bill?\n"))
bill_with_tip = (tip/100)*bill + bill
bill_per_person = bill_with_tip/people
final_amount_per_person = round(bill_per_person, 2)
print(f"Total bill is: ${bill_with_tip}")
print(f"And each person will pay: ${final_amount_per_person}.")