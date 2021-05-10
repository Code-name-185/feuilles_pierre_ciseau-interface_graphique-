from Tkinter import * 
import jeu

root = Tk(className ="Pierre Feuille Ciseau")
root.resizable(0,0)

svalue = IntVar()
pfc = jeu.Jeu()

def nouvellePartie():
    pfc.scoreJoueur = 0
    pfc.scoreOrdi = 0
    updatescore("                                                  ")
    
    buttonCaillou = Button(root,text="Pierre", command=choixCaillou) 
    buttonCaillou.grid(row = 1, column = 0, padx = 5, pady =5)

    buttonFeuille = Button(root,text="Feuille", command=choixFeuille) 
    buttonFeuille.grid(row = 1, column = 1, padx = 5, pady =5)

    buttonCiseau = Button(root,text="Ciseau", command=choixCiseau) 
    buttonCiseau.grid(row = 1, column = 2, padx = 5, pady =5)

    buttonFin = Button(root,text="Fin de partie", command=finDePartie) 
    buttonFin.grid(row = 3, column = 1, padx = 5, pady =5)

def choixCaillou():
    res = pfc.round(pfc.choix[0], pfc.choixOrdi1())
    updatescore("                                                  ")
    updatescore(res)

def choixFeuille():
    res = pfc.round(pfc.choix[1], pfc.choixOrdi1())
    updatescore("                                                            ")
    updatescore(res)
    
def choixCiseau(): 
    res = pfc.round(pfc.choix[2], pfc.choixOrdi1())
    updatescore("                                                            ")
    updatescore(res)

def updatescore(res):
    scoreJ = Label(root, text= "Joueur " + str(pfc.scoreJoueur))
    scoreJ.grid(row = 2, column = 0, padx = 5, pady =5)
    scoreO = Label(root, text= "Ordinateur " + str(pfc.scoreOrdi))
    scoreO.grid(row = 2, column = 2, padx = 5, pady =5)
    scoreT = Label(root, text = res)
    scoreT.grid(row = 2, column = 1, padx = 5, pady =5)

def finDePartie():
    pfc.finPartie()
    if pfc.scoreJoueur > pfc.scoreOrdi:
            victoireJoueur = Label(root, text= "Le joueur a gagné avec " + str(pfc.scoreJoueur) + " et l'ordi " +str(pfc.scoreOrdi))
            victoireJoueur.grid(row = 4, column = 1, padx = 5, pady =5)
    elif pfc.scoreJoueur < pfc.scoreOrdi:
            victoireOrdi = Label (root, text=  "L'ordi a gagné avec " + str(pfc.scoreOrdi) + " et le joueur " +str(pfc.scoreJoueur))
            victoireOrdi.grid(row = 4, column = 1, padx = 5, pady =5)
    else:
            egalite = Label(root, text= "égalité, les deux ont " + str(pfc.scoreJoueur))
            egalite.grid(row = 4, column = 1, padx = 5, pady =5)

buttonNouvellePartie = Button(root,text="NouvellePartie", command=nouvellePartie) 
buttonNouvellePartie.grid(row = 0, column = 1, padx=10, pady =10)

root.mainloop()