
hrs = input("Enter Hours:")
h = float(hrs)

rate = float(input("Enter Rate:"))

if (h > 40):
    salary = 40*rate + 1.5*(h-40)*rate
else:
    salary =h*rate

print(salary)