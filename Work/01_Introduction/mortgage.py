# mortgage.py
#
# Exercise 1.7
principal = 500000.0
remaining_principal = principal
rate = 0.05
payment = 2684.11

extra_payment_start_month = int(input("Enter extra payment start month: "))
extra_payment_end_month = int(input("Enter extra payment end month: "))
extra_payment = float(input("Enter extra payment amount: "))

total_paid = 0.0
total_months = 0

while principal > 0:

    actualPayment = payment + extra_payment if total_months >= extra_payment_start_month and total_months <= extra_payment_end_month else payment
    principalWithInterest = principal * (1 + rate / 12)

    # to prevent overcharging just pay remaining principal if less than actual payment
    actualPayment = principalWithInterest if principalWithInterest < actualPayment else actualPayment
    principal = principalWithInterest - actualPayment
    total_paid = total_paid + actualPayment

    total_months = total_months + 1
    print(f'{total_months}\t£{round(total_paid,2)}\t£{round(principal, 2)}')

print("Total Paid", round(total_paid, 2))
print("Total Months", total_months)