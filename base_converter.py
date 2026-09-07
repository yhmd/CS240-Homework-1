#baseconverter
print("Choose the original base:")
print("1 - Binary")
print("2 - Decimal")
print("3 - Octal")
print("4 - Hexadecimal")

choice = input("Enter your choice: ")
number = input("Enter the number: ")

try:
    if choice == "1":
        decimal = int(number, 2)

    elif choice == "2":
        decimal = int(number, 10)

    elif choice == "3":
        decimal = int(number, 8)

    elif choice == "4":
        decimal = int(number, 16)

    else:
        print("Invalid choice")
        exit()

    print("")
    print("Binary:", bin(decimal))
    print("Decimal:", decimal)
    print("Octal:", oct(decimal))
    print("Hexadecimal:", hex(decimal).upper())

except ValueError:
    print("This number is not valid for the selected base.")