tip = int(input("enter the tip percentage"))
bill = int(input("enter the bill amount"))
def total_calc(bill,tip):
 total = (bill + (tip/100)*bill)
 print (f"the amount is {total}")
total_calc(bill,tip)
    