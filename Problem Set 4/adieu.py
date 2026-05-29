import inflect
p = inflect.engine()

name = []
while True:

    try:
        k = input("Name: ")
        name.append(k)

    except EOFError:
        break

print(f"\nAdieu, adieu, to {p.join(name)}")
