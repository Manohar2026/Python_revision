def is_prime(n):
    if n<2:
        return None
    elif n==2:
        return True
    else:
        for i in range(3,int(n**0.5)+1,2):
            if n%i == 0:
                return False
        return True
        
try:
    num = int(input("Enter your number : "))
    
    result = is_prime(num)
    
    if result == None:
        print(f"{num} is neither prime nor composite")
    elif result:
        print(f"{num} is prime")
    else:
        print(f"{num} is composite")
        
except ValueError:
    print("Invalid input")