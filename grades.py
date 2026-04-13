print("enter 5 subject  marks")
tot=0
for i in range(1,6):
    m=int(input("enter marks:"))
    tot=tot+m
print("aggregate(total)=",tot)
percentage=(tot/500)*100
print("percentage of marks:",percentage)
if percentage>=90:
    print("grade:O")
elif percentage>=80:
    print("grade:A+")
elif percentage>=70:
    print("grade:A:")
elif percentage>=60:
    print("grade:B+")
elif percentage>=55:
    print("grade:B:")
elif percentage>=50:
    print("grade:C")
else:
    print("invalid")
