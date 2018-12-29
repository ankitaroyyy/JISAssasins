#26
bsalary =int(input("Enter basic salary"))
if bsalary>=5000:
    hra=15*bsalary/100
    da=150*bsalary/100
elif bsalary<5000:
    hra=10*bsalary/100
    da=110*bsalary/100
gsalary = bsalary+hra+da
print(gsalary)