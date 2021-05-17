from Tkinter import * 
import jeu

root = Tk(className ="Caillou Feuille Ciseau")
root.resizable(0,0)

svalue = StringVar()
pfc = jeu.Jeu()

svalue = StringVar()

def nouvellePartie():
    pfc.scoreJoueur = 0
    pfc.scoreOrdi = 0
    updatescore("                                                  ","","")
    
    buttonCaillou.grid(row = 2, column = 0, padx = 5, pady =5)

    buttonFeuille.grid(row = 2, column = 1, padx = 5, pady =5)

    buttonCiseau.grid(row = 2, column = 2, padx = 5, pady =5)

    prenom.grid_forget()
    nom.grid_forget()
    victoireJoueur.grid_forget()
    victoireOrdi.grid_forget()
    egalite.grid_forget()


#Le p (ChoixP) correspond à pierre (caillou)

def choixCaillou():
    choixP = pfc.choixOrdi1() 
    res = pfc.round(pfc.choix[0], choixP)
    updatescore("                                                  ","","")
    updatescore(res,pfc.choix[0],choixP)
    if pfc.scoreJoueur  == 3:
        finDePartie()
    elif pfc.scoreOrdi == 3:
        finDePartie()

def choixFeuille():
    choixF = pfc.choixOrdi1() 
    res = pfc.round(pfc.choix[1], choixF)
    updatescore("                                                  ","","")
    updatescore(res,pfc.choix[1],choixF)
    if pfc.scoreJoueur  == 3:
        finDePartie()
    elif pfc.scoreOrdi == 3:
        finDePartie()
    
def choixCiseau():
    choixC = pfc.choixOrdi1() 
    res = pfc.round(pfc.choix[2], choixC)
    updatescore("                                                  ","","")
    updatescore(res, pfc.choix[2], choixC)
    if pfc.scoreJoueur == 3:
        finDePartie()
    elif pfc.scoreOrdi == 3:
        finDePartie()

def updatescore(res, choixJoueur, choixOrdi):
    resultatJeu = Label(root, text = "             -             ")
    resultatJeu.grid(row = 3, column = 1, padx = 5, pady = 5)
    resultatJeu = Label(root, text = choixJoueur + " - " + choixOrdi)
    resultatJeu.grid(row = 3, column = 1, padx = 5, pady = 5)
    scoreJ = Label(root, text= "                                  ")
    scoreJ.grid(row = 4, column = 0, padx = 5, pady =5)
    scoreJ = Label(root, text= svalue.get() + " " + str(pfc.scoreJoueur))
    scoreJ.grid(row = 4, column = 0, padx = 5, pady =5)
    scoreO = Label(root, text= "Ordinateur " + str(pfc.scoreOrdi))
    scoreO.grid(row = 4, column = 2, padx = 5, pady =5)
    scoreT = Label(root, text = res)
    scoreT.grid(row = 4, column = 1, padx = 5, pady =5)

def finDePartie():
    pfc.finPartie()
    if pfc.scoreJoueur > pfc.scoreOrdi:
        victoireJoueur.update()
        victoireJoueur.grid(row = 6, column = 1, padx = 5, pady =5)
    elif pfc.scoreJoueur < pfc.scoreOrdi:
        victoireOrdi.grid(row = 6, column = 1, padx = 5, pady =5)
    else:
        egalite.grid(row = 6, column = 1, padx = 5, pady =5)

    svalue.set("")
    prenom.grid(row = 1, column = 1, padx=10, pady =10)
    nom.grid(row = 1, column = 0, padx = 5, pady =5)
    buttonCaillou.grid_forget()

    buttonFeuille.grid_forget()
    buttonCiseau.grid_forget()
    buttonNouvellePartie.destroy()

    buttonRecommencer = Button(root,text="Recommencer", command=nouvellePartie)
    buttonRecommencer.grid(row = 0, column = 1, padx=10, pady =10)

def quitter():
    
    root.destroy()
        
buttonNouvellePartie = Button(root,text="Nouvelle partie", command=nouvellePartie) 
buttonNouvellePartie.grid(row = 0, column = 1, padx=10, pady =10)

buttonQuitter = Button(root,text="Quitter", command=quitter, bg="red") 
buttonQuitter.grid(row = 0, column = 2, padx=10, pady =10)

buttonCaillou = Button(root,text="Caillou", command=choixCaillou)
buttonFeuille = Button(root,text="Feuille", command=choixFeuille) 
buttonCiseau = Button(root,text="Ciseau", command=choixCiseau) 

nom = Label(root, text = "Nom du joueur : ")
nom.grid(row = 1, column = 0, padx = 5, pady =5)
prenom = Entry(root, textvariable = svalue)
prenom.grid(row = 1, column = 1, padx=10, pady =10)

victoireJoueur = Label(root, text= "Bravo, vous avez gagné !")
victoireOrdi = Label (root, text= "Schade, l'ordinateur a gagné")

root.mainloop()