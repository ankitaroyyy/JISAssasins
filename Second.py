#7
num = int(input("Enter number"))
tot=0
while(num>0):
    dig=num%10
    tot+=dig
    num=num//10
print(tot)
