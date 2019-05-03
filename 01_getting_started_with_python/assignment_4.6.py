

def computepay(h,r):
    h = float(h)
    r = float(r)

    if h <= 40:
        salary = h*40
    else:
        salary = 40 * r + 1.5 * (h - 40) * r

    return salary

hrs = input("Enter Hours:")
rate = input("Enter rate:")
p = computepay(hrs, rate)
print(p)