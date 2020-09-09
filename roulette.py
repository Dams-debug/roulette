from random import *
"""

-- Roulette russe --

1- Attribuer un solde à chaque joueur
2- Tant que le joueur a suffisament d'argent, il peut :
	- choisir un nombre
	- choisir une couleur
	- miser une somme
3- Si la mise est bonne (couleur + valeur):
	- mise doublée
4- Si la mise est partiellement bonne (soit couleur soit valeur):
	- mise rendu
5- Si la mise n'est pas bonne:
	-mise perdue
6- Modification du solde du joueur.

"""

# Attribution du solde du joueur + affichage du message de bienvenue.
print("---------------------------------------------")
print("|                                           |")
print("|          -- JEU DU GRAND CASINO --        |")
print("|             ___________________           |")
print("---------------------------------------------")

soldeDuJoueur = int(100)
print("Bonjour et bienvenue à cette table, votre solde est de",soldeDuJoueur,"euros.")

while soldeDuJoueur >= 10:

	sommeJouee = int(input("Veuillez choisir la somme à miser (cette dernière doit être supérieur à 10) : "))

	if sommeJouee > 10 and sommeJouee <= soldeDuJoueur:
		
		numeroAJouer = int(input("Veuillez choisir un numéro sur lequel jouer (1 - 20) : "))
		
		if numeroAJouer >= 1 and numeroAJouer <= 20:
			
			couleurAJouer = str(input("Veuillez choisir une couleur | (r)ouge ou (n)oir | : "))
			
			if couleurAJouer == str("n") or couleurAJouer == str("r"):
				
				print("Les jeux sont fait, RIEN NE VA PLUS !")
				numGagnant = randrange(1, 20)
				couleurGagnante = choice(["n","r"])
				couleurAnnonce = "default"

				if couleurGagnante == ("n"):
					couleurAnnonce = "noir"

				elif couleurGagnante == ("r"):
					couleurAnnonce = "rouge"

				print("C'est le", numGagnant,couleurAnnonce, "qui l'emporte !")

				if numeroAJouer == numGagnant and couleurAJouer == couleurGagnante:
					print("Félicitations, vous doublez votre mise !")
					soldeDuJoueur += (sommeJouee) * 2
					print("Votre solde : ",soldeDuJoueur,"euros.")
				elif numeroAJouer == numGagnant and couleurAJouer != couleurGagnante:
					print("Numéro gagnant !")
					soldeDuJoueur += (sommeJouee) / 2
					print("Votre solde : ",soldeDuJoueur,"euros.")
				elif numeroAJouer != numGagnant and couleurAJouer == couleurGagnante:
					print("Couleur gagnante !")
					soldeDuJoueur -= (sommeJouee) / 2
					print("Votre solde : ",soldeDuJoueur,"euros.")
				else:
					print("Perdu")
					soldeDuJoueur -= sommeJouee
					print("Votre solde : ",soldeDuJoueur,"euros.")
			
			else:
				
				print("Réponse non valide, veuillez renseigner dans le champs suivant :")
				print("- r pour rouge")
				print("- n pour noir")
		
		else:
			
			print("Réponse non valide, veillez à bien choisir un numéro compris entre 1 et 20 !")

	else:
		print("Désolé, vous ne pouvez pas miser cette somme car elle est soit inférieur à 10€ soit elle est supérieur à votre solde !")

if soldeDuJoueur < 10:
	print("Désolé monsieur vous n'avez plus assé d'argent, votre solde est de :", soldeDuJoueur,"euros.")
	print("Au revoir !")
