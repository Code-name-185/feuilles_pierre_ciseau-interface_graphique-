# -*- coding: utf-8 -*-

from Tkinter import * 
import jeu

root = Tk(className ="Pierre Feuille Ciseau") 

svalue = IntVar()
pfc = jeu.Jeu()

def choixCaillou(): 
    pfc.round(pfc.choix[0], pfc.choixOrdi1())
    score = Label(root, text = "Score de Joueur " + str(pfc.scoreJoueur) + " Score de l'ordi " + str(pfc.scoreOrdi))
    score.pack()

def choixFeuille(): 
    pfc.round(pfc.choix[1], pfc.choixOrdi1())
    score = Label(root, text = "Score de Joueur " + str(pfc.scoreJoueur) + " Score de l'ordi " + str(pfc.scoreOrdi))
    score.pack()
    
def choixCiseau(): 
    pfc.round(pfc.choix[2], pfc.choixOrdi1())
    score = Label(root, text = "Score de Joueur " + str(pfc.scoreJoueur) + " Score de l'ordi " + str(pfc.scoreOrdi))
    score.pack()

def finDePartie():
    pfc.finPartie()

def close_window():
    root.destroy()

buttonCaillou = Button(root,text="Pierre", command=choixCaillou) 
buttonCaillou.pack()

buttonFeuille = Button(root,text="Feuille", command=choixFeuille) 
buttonFeuille .pack()

buttonCiseau = Button(root,text="Ciseau", command=choixCiseau) 
buttonCiseau.pack()

buttonFin = Button(root,text="Fin de partie", command=finDePartie) 
buttonFin.pack()

buttonquit = Button(text = "Quit", command = close_window)
buttonquit.pack()

root.mainloop()
