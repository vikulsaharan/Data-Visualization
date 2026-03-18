n = int(input("Enter number of persons: "))

for i in range(n):
    print("\nPerson", i+1)
    
    p = float(input("Enter P: "))
    r = float(input("Enter R: "))
    t = float(input("Enter T: "))

    si = (p * r * t) / 100
    print("Simple Interest:", si)