print("Bienvenue à Python !")

nom = "Python"
print("Bonjour, je suis " + nom)

prenom = input("Et vous quel est votre nom ? ")

print("Bonjour, " + prenom)

def afficher_message(nom):
    print("Bonjour, " + nom)

for i in range(1, 6):
    print(i)

def demander_nombres():
    print("Entrez le premier nombre:")
    num1 = int(input())
    print("Entrez le deuxième nombre:")
    num2 = int(input())
    return num1, num2

while True:
    num1, num2 = demander_nombres()
    if num1 == num2:
        print("Bravo, vous avez compris les opérateurs logiques")
        break
    else:
        print("Non, les deux nombres ne sont pas les mêmes.")
