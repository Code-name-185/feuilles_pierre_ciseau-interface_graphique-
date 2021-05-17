# -*- coding: utf-8 -*-
from random import *

class Jeu:

    scoreJoueur = 0
    scoreOrdi = 0
    choix = ["Caillou", "Feuille", "Ciseau"] 

    def round (self,choixjoueur, choixordi):
        if choixjoueur == self.choix[0] and choixordi == self.choix[1]:
            self.scoreOrdi += 1
            print("L'ordinateur gagne le point")
            return("L'ordinateur gagne le point")
        elif choixjoueur == self.choix[0] and choixordi == self.choix[2]:
            self.scoreJoueur += 1
            print("Vous gagnez le point")
            return("Vous gagnez le point")
        elif choixjoueur == self.choix[1] and choixordi == self.choix[0]:
            self.scoreJoueur += 1
            print("Vous gagnez le point")
            return("Vous gagnez le point")
        elif choixjoueur == self.choix[1] and choixordi == self.choix[2]:
            self.scoreOrdi += 1
            print("L'ordinateur gagne le point")
            return("L'ordinateur gagne le point")
        elif choixjoueur == self.choix[2] and choixordi == self.choix[0]:
            self.scoreOrdi += 1
            print("L'ordinateur gagne le point")
            return("L'ordinateur gagne le point")
        elif choixjoueur == self.choix[2] and choixordi == self.choix[1]:
            self.scoreJoueur += 1
            print("Vous gagnez le point")
            return("Vous gagnez le point")
        else:
            print("Personne ne gagne le point")
            return("Personne ne gagne le point")

    def choixOrdi1(self):
        choi = randrange(3)
        if choi == 0:
            return self.choix[0]
        elif choi == 1:
            return self.choix[1]
        else:
            return self.choix[2]

    def finPartie (self):
        if self.scoreJoueur > self.scoreOrdi:
            print "Le joueur a gagné avec " + str(self.scoreJoueur) + " et l'ordi a " +str(self.scoreOrdi)
        elif self.scoreJoueur < self.scoreOrdi:
            print "L'ordi a gagné avec " + str(self.scoreOrdi) + " et le joueur a " +str(self.scoreJoueur)
        else:
            print "égalité, les deux ont " + str(self.scoreJoueur)
        
    

