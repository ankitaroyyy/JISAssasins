#10
X = input("Enter your string")

newstr = X;
print("\nRemoving vowels from the given string...");
vowels = ('a', 'e', 'i', 'o', 'u');
for x in X.lower():
    if x in vowels:
        newstr = newstr.replace(x, "");
print("New string after successfully removed all the vowels:");
print(newstr);