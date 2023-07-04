weight = input("Weight: ")
unit = input("L(lbs) or K(Kg)? ")

if unit.upper() == "L":
    print(f"You are {int(weight)*0.45} kilos")
elif unit.upper() == "K":
    print(f"You are {int(weight)*2.2} pounds")
else:
    print("Please double-check if you have entered the right unit")

# Secondary Way(a little shorter):
# weight = int(input("Weight: "))
# unit = input("L(lbs) or K(Kg)? ")
#
# if unit.upper() == "L":
#     converted = weight * 0.45
#     print(f"You are {converted} kilos")
# elif unit.upper() == "K":
#     converted = weight * 2.2
#     print(f"You are {converted} pounds")
# else:
#     print("Please double-check if you have entered the right unit")
