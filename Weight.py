weight = int(input("weight:"))
unit = input('(L) or (K):')
if unit.upper() == "L":
    converted = weight * 0.45
    print(f"you are {converted} kg")
else:
    converted = weight / 0.45
    print(f'you are {converted} lbs')

