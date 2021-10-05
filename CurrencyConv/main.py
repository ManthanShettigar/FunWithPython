with open('data.txt') as f:
	lines = f.readlines()

CDictionary = {}
for line in lines:
	parsed = line.split("\t")
	CDictionary[parsed[0]] = parsed[1]

amt = int(input(" \n***Please enter the Ammount***\n"))
print(" \nCurrency options--\n")
[print(item) for item in CDictionary.keys()]
Curr = input("\nSelect and enter the name of the currency-\n")
print(f"{amt} INR = {amt *float(CDictionary[Curr])} {Curr}")
print("currency successfully converted!")