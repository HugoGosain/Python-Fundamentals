# # if bill > $100 --> members get 25% discount / non members 15%
# # $50-$100 member -> 10% / non -> 5%
# # <50, no discount

# cost = float(input("How much was your bill? "))
# status = input("Are you a member? ").lower()
# date = input("is it the weekend? ").lower()

# if cost > 100 and status == "yes" and date == "no":
#     discount = (25/100)*cost
#     bill = cost-discount
#     print(bill)
# elif cost > 100 and status == "no" and date == "no":
#     discount = (15/100)*cost
#     bill = cost-discount
#     print(bill)
# elif (cost <= 100 and cost >= 50) and status == "yes" and date == "no":
#     discount = (10/100)*cost
#     bill = cost-discount
#     print(bill)
# elif (cost <= 100 and cost >= 50) and status == "no" and date == "no":
#     discount = (5/100)*cost
#     bill = cost-discount
#     print(bill)
# elif cost > 100 and status == "yes" and date == "yes":
#     discount = (25/100)*cost
#     service = (5/100)*cost
#     bill = cost-discount+service
#     print(bill)
# elif cost > 100 and status == "no" and date == "yes":
#     discount = (15/100)*cost
#     service = (5/100)*cost
#     bill = cost-discount+service
#     print(bill)
# elif (cost <= 100 and cost >= 50) and status == "yes" and date == "yes":
#     discount = (10/100)*cost
#     service = (5/100)*cost
#     bill = cost-discount+service
#     print(bill)
# elif (cost <= 100 and cost >= 50) and status == "no" and date == "yes":
#     discount = (5/100)*cost
#     service = (5/100)*cost
#     bill = cost-discount+service
#     print(bill)
# elif cost < 50 and date == "yes":
#     service = (5/100)*cost
#     bill = cost+service
#     print (bill)
# else:
#     print(cost)

cost = float(input("How much was your bill? "))
status = input("Are you a member? ").lower()
date = input("is it the weekend? ").lower()
discount = 0
service = 0

if cost > 100:
    if status == "yes":
        discount = 0.25
    else:
        discount = 0.15
elif 50 <= cost <= 100:
    if status == "yes":
        discount = 0.10
    else:
        discount = 0.05
else:
    discount = 0

discountamount = cost*discount
finalbill = cost-discountamount

if date == "yes":
    service = finalbill*0.05
    finalbill = finalbill+service
else:
    service = 0

print (f"\n-----BILL DETAILS-----\n Original Bill: ${cost} \n Discount amount: ${discountamount} \n Service charge: ${service} \n Final amount to pay: ${finalbill}")