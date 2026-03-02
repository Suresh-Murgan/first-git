def add(a, b):
    return a + b

print("1.Addition")
print("2.Exit")

status = True

while status:
    choice = int(input("Enter the Choice : "))

    match choice:
        case 1:
            num1 = int(input("Enter the Num 1 : "))
            num2 = int(input("Enter the Num 2 : "))
            print(add(num1, num2))
            print("--------------------")
        case 2:
            status = False
        case _:
            print("Enter a valid Option...")