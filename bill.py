"""a) Write a python script to calculate electricity bill based on following slab
rates.
Consumption units Rate (in Rupees/Unit)
0-100           4
101-150        4.6
151-200        5.2
201-300        6.3
Above 300       8
(Hint: To get Consumption units take current meter reading and old meter
reading from the user as input)"""

curr=int(input("enter curr readings : "))
old=int(input("enter old readings : "))
units=curr-old
print("units : ",units)
if units>=0 and units<=100:
    bill= units*4
elif units>=101 and units<=150: 
    bill=(100*4)+(units-100)*4.6
elif units>=151 and units<=200:
    bill=(100*4)+(50*4.6)+(units-150)*5.2
elif units>=201 and units<=s300:
    bill=(100*4)+(50*4.6)+(50*5.2)+(units-200)*6.3
elif units>300:
    bill=(100*4)+(50*4.6)+(50*5.2)+(100*6.3)+(unit-300)*8
  
print("bill : ",bill)

 
