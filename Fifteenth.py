#9
num=int(input("Enter the number"))
ld=num%10
fd=num
while(num>=10):
    num=num//10
fd=num
sum=fd+ld
print("The sum of first and last digit of the number is",sum)