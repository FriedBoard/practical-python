# mortgage.py
#
# Exercise 1.7
lend = 500000
rate = 0.05
payment = 2684.11
total_Paid = 0
extra_Payment_Start_Month = 61
extra_Payment_End_Month = 108
extra_Payment = 1000
month = 0


while lend > 0:
    month = month + 1
    loop_Payment = payment
    
    if month >= extra_Payment_Start_Month and month <= extra_Payment_End_Month:
        lend = lend * (1+rate/12) - payment - extra_Payment
        loop_Payment = loop_Payment + extra_Payment
    else:
        if lend - loop_Payment < 0:
            loop_Payment = lend
            lend = lend-lend
        else:
            lend = lend * (1+rate/12) - payment
    total_Paid = total_Paid + loop_Payment
    print(month, total_Paid, lend)

print(' Total paid', round(total_Paid, 2))