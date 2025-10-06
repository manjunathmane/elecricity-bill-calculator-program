units=int(input("Enter the number of units consumed:"))
total=units*5
print("Units Consumed:₹",units)
print("Total Bill:₹",{total})
disc=total*0.10
final1=total   #without discount
final2=total-disc    #with discount
if total>=1001:
    print("Discount Applied:₹" ,disc)
    print("Final Bill:₹" ,final2)
else:
    print("Final Bill:₹" ,final1)

