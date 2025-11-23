decimal = int(input("Enter a decimal number: "))
num = decimal
binary = ""
while num > 0:
    remainder = num % 2   # find bit
    binary = str(remainder) + binary
    for i in range(1):
        pass
    num = num // 2
print("Binary of", decimal, "is:", binary)
