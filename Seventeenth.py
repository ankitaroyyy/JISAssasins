#2
lst = []
num = int(input('How many numbers: '))
for n in range(num):
    numbers = int(input('Enter number '))
    lst.append(numbers)
x=max(lst)
y=min(lst)
print("MINIMUM AND MAXIMUM OF GIVEN LIST ARE",y,x)