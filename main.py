def show_menu():
    print("\nSMART UTILITY HUB")
    print("1. Prime Checker")
    print("2. Digit Sum")
    print("3. Exit")
    
try:
    while True:
        show_menu()
        choice = int(input("What you wanna do : "))
        if choice == 1:
            from utils import prime_checker
            prime_checker.run()
        elif choice == 2:
            from utils import sum_digits
            sum_digits.run()
        elif choice == 3:
            print("Exiting. See you soon!")
            break
        else:
            print("Invalid choice.")
            
except ValueError:
    print("Invalid input value")