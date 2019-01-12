"""Anna Markiewicz
Project 1
Due Date: Jan 17
Submission Date: Jan 11"""

def get_user_input(message):
    result = float(input(f"{message}:"))
    if result < 0:
        print("This is an error message, please enter higher number")
        #exit()
    else:
        return result

def get_monthly_payment(principal, rate, num_payments):
    monthly_payment = principal * ((rate * ((1+rate) ** num_payments)) / ((1+rate) ** num_payments - 1))
    return round(monthly_payment,2)



principal = get_user_input("Enter amount of loan")
rate = get_user_input("Interest rate in percent i.e. 5") / 100 / 12
num_years = get_user_input("Number of years")
num_payments = 12 * num_years


monthly_payment= get_monthly_payment(principal, rate, num_payments)

print(f"your monthly payment is: ${monthly_payment}")
