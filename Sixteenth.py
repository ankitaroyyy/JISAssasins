#11
X = input("Enter your string")
Y = input("Enter your character")
count = 0

for i in X:
    if i == Y:
        count = count + 1
print(count)