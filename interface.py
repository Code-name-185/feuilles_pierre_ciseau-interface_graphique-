# -*- coding: utf-8 -*-

from Tkinter import * 
import jeu

root = Tk(className ="Pierre Feuille Ciseau") 

svalue = IntVar()
pfc = jeu.Jeu()

def nouvellePartie():
    pfc.scoreJoueur = 0
    pfc.scoreOrdi = 0
    
    buttonCaillou = Button(root,text="Pierre", command=choixCaillou) 
    buttonCaillou.grid(row = 2, column = 1)

    buttonFeuille = Button(root,text="Feuille", command=choixFeuille) 
    buttonFeuille.grid(row = 2, column = 2)

    buttonCiseau = Button(root,text="Ciseau", command=choixCiseau) 
    buttonCiseau.grid(row = 2, column = 3)

    buttonFin = Button(root,text="Fin de partie", command=finDePartie) 
    buttonFin.grid(row = 3, column = 2)

def updatescore():
    pass

def choixCaillou():
    pfc.round(pfc.choix[0], pfc.choixOrdi1())
    updatescore()

def choixFeuille():
    pfc.round(pfc.choix[1], pfc.choixOrdi1())
    updatescore()
    
def choixCiseau(): 
    pfc.round(pfc.choix[2], pfc.choixOrdi1())
    updatescore()

def finDePartie():
    pfc.finPartie()
    if pfc.scoreJoueur > pfc.scoreOrdi:
            victoireJoueur = Label(root, text= "Le joueur a gagné avec " + str(pfc.scoreJoueur) + " et l'ordi " +str(pfc.scoreOrdi))
            victoireJoueur.pack()
    elif pfc.scoreJoueur < pfc.scoreOrdi:
            victoireOrdi = Label (root, text=  "L'ordi a gagné avec " + str(pfc.scoreOrdi) + " et le joueur " +str(pfc.scoreJoueur))
            victoireOrdi.pack()
    else:
            egalite = Label(root, text= "égalité, les deux ont " + str(pfc.scoreJoueur))
            egalite.pack()

def close_window():
    root.destroy()

buttonNouvellePartie = Button(root,text="NouvellePartie", command=nouvellePartie) 
buttonNouvellePartie.pack()

buttonquit = Button(text = "Quit", command = close_window)
buttonquit.pack()

root.mainloop()
