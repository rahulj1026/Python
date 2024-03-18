while True:
    try:
        n=int(input("Enter a number "))
        print(f"You entered the number {n}")
        break
    except ValueError:
        print("Wrong Number, Enter a valid number. Try Again...")
    finally:
        print("Hurray, Program ran successfully even with the exception")
