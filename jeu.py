from random import *

class Jeu:

    scoreJoueur = 0
    scoreOrdi = 0
    choix = ["pierre", "feuille", "ciseau"] 

    def round (self,choixjoueur, choixordi):
        if choixjoueur == self.choix[0] and choixordi == self.choix[1]:
            self.scoreOrdi += 1
            print("L'ordinateur a gagné")
        elif choixjoueur == self.choix[0] and choixordi == self.choix[2]:
            self.scoreJoueur += 1
            print("Le joueur a gagné")
        elif choixjoueur == self.choix[1] and choixordi == self.choix[0]:
            self.scoreJoueur += 1
            print("Le joueur a gagné")
        elif choixjoueur == self.choix[1] and choixordi == self.choix[2]:
            self.scoreOrdi += 1
            print("L'ordinateur a gagné")
        elif choixjoueur == self.choix[2] and choixordi == self.choix[0]:
            self.scoreOrdi += 1
            print("L'ordinateur a gagné")
        elif choixjoueur == self.choix[2] and choixordi == self.choix[1]:
            self.scoreJoueur += 1
            print("Le joueur a gagné")
        else:
            print("égalité")

    def choixOrdi1(self):
        choi = randrange(3)
        if choi == 0:
            return self.choix[0]
        elif choi == 1:
            return self.choix[1]
        else:
            return self.choix[2]
    
#pfc = Jeu()
#pfc.round(pfc.choix[1], pfc.choixOrdi1())