def LCM (a,b):
    n = 1
    while True:
        if n % a == 0 and n % b == 0:
            print (f"The LCM of {a} and {b} is {n}")
            break
        n += 1
LCM (99,9987)