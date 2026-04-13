a=int(input("enter the salary of the employee:"))
b=int(input("enter the leave days:"))
if b<=2:
   print("no reduction in salary")
   print("salary=",a)
else:
   c=(b-2)*500
   print("salary=",a-c)
