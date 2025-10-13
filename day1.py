import random
rice=45
sugar=40
oil=130
ricebrought=3
sugarbrought=2.5
oilbrought=1.8

totalrice=rice*ricebrought
totalsugar=sugar*sugarbrought
totaloil=oil*oilbrought
print("Total price of rice=",totalrice)
print("Total price of sugar=",totalsugar)
print("Total price of oil=",totaloil)

total_bill=totalrice+totalsugar+totaloil
print("Total price=",total_bill)

total_bill_int=int(total_bill)
print("Total price in integer=",total_bill_int)

total_bill_str=str(total_bill)
print("Total price in string=",total_bill_str)

delivery_charge=random.randint(5,10)
print("Delivery Charge=",delivery_charge)

final_bill=total_bill+delivery_charge
print("Final Bill=",final_bill)
