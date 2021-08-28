largest = None
smallest = 3
while True:
    num = input("Enter a number: ")
    if num == "done" : 
        break
    try :
       num = int(num)
       if num < smallest:
            smallest = num
       if num > largest:
            largest = num
       continue
    except:
       print("Invalid input")
        
print("Maximum is", largest)
print("Minimum is", smallest)