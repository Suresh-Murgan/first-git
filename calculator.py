def add(a, b):
    return a + b

def sub(a,b):
    return a - b 

print("--------------------")
print("1.Addition")
print("2.Subtraction")
print("3.Exit")
print("--------------------")

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
            num1 = int(input("Enter the Num 1 : "))
            num2 = int(input("Enter the Num 2 : "))
            print(sub(num1, num2))
            print("--------------------")
        
        case 3:
            exit()
        
        case _:
            print("Enter a valid Option...")