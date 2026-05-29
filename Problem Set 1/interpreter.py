x, y, z = input("Enter an expression: ").split(" ")

x, z = float(x), float(z)

if y == "+":
    print(round(x + z, 1))
elif y == "-":
    print(round(x - z,1))
elif y == "*":
    print(round(x * z, 1))
elif y == "/":
    print(round(x / z, 1))

