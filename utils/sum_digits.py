def sums(n):
    sum_digit = 0
    while n>0:
        a = n % 10
        sum_digit += a
        n = n // 10
    return sum_digit

def run():
    try:
        num = int(input("Enter the number : "))
        
        result = sums(num)
        
        print(f"Sums of the digits of {num} is {result}")

    except ValueError:
        print("Invalid input!")