# asking the user to enter n
n = int(input("Entrez un entier n : "))

Un = 6

# Calculating the value of Un
for i in range(1, n + 1):
    Un = 4 * Un + 10

# Printing the result
print("La valeur est :", Un)
