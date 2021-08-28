def computepay(h,r):
    if h > 40:
    	h = 40 + (h - 40)*1.5
    return h*r

hrs = input("Enter Hours:")
rate = input("Enter Rates:")
h = float(hrs)
r = float(rate)
p = computepay(h,r)
print("Pay",p)