#PROJET QRCODE DONT LE BUT EST DE DECODER UN QRCODE#

#version non officiel


# importation de librairies
import tkinter as tk
import PIL as pil
from PIL import Image
from PIL import ImageTk 



#constantes
HAUTEUR= 500
LARGEUR= 500



#fonctions

def nbrCol(matrice):
    return(len(matrice[0]))

def nbrLig(matrice):
    return len(matrice)


def saving(matPix, filename):#sauvegarde l'image contenue dans matpix dans le fichier filename
							 #utiliser une extension png pour que la fonction fonctionne sans perte d'information
    toSave=pil.Image.new(mode = "1", size = (nbrCol(matPix),nbrLig(matPix)))
    for i in range(nbrLig(matPix)):
        for j in range(nbrCol(matPix)):
            toSave.putpixel((j,i),matPix[i][j])
    toSave.save(filename)

def loading(filename):#charge le fichier image filename et renvoie une matrice de 0 et de 1 qui représente 
					  #l'image en noir et blanc
    toLoad=pil.Image.open(filename)
    mat=[[0]*toLoad.size[0] for k in range(toLoad.size[1])]
    mat_modif=[[0]*toLoad.size[0] for k in range(toLoad.size[1])]
    for i in range(toLoad.size[1]):
        for j in range(toLoad.size[0]):
            mat[i][j]= 0 if toLoad.getpixel((j,i)) == 0 else 1
    return mat, mat_modif


#matrice représentatnt le symbol carré entouré ligne blanche entouré ligne noir, le 0 représente le noir et le 1 le blanc, c'est peut être a interchanger je sais pas trop faut tester et je peux pas atm
symbole = [[0, 0, 0, 0, 0, 0, 0, 1], 
           [0, 1, 1, 1, 1, 1, 0, 1], 
           [0, 1, 0, 0, 0, 1, 0, 1], 
           [0, 1, 0, 0, 0, 1, 0, 1], 
           [0, 1, 0, 0, 0, 1, 0, 1], 
           [0, 1, 1, 1, 1, 1, 0, 1], 
           [0, 0, 0, 0, 0, 0, 0, 1],
           [1, 1, 1, 1, 1, 1, 1, 1]]




    
def rotate(mat):
    """effectue une rotation a l'image afin de la remettre à l'endroit"""
    mat_tempo = []
    for i in range(25):
        tempo = []
        for j in range(25-1,-1,-1):     # j va de -1 a -25
            tempo.append(mat[j][i])     # on recopie la colonne i sur la ligne i
        mat_tempo.append(tempo)         # on l'ajoute dans une matrice temporaire
    for i in range(25):
        for j in range(25):
            mat[i][j] = mat_tempo[i][j] # on réécrit la matrice 
    return mat

            

def verify(mat) :
    """vérifie si la matrice est dans le bon sens"""
    cpt = 0
    verifie = True
    while verifie == True :
        for i in range(len(symbole)) :
                for j in range(len(symbole)) :
                    for k in symbole[i][j] :
                        if k == mat[-8+i][-8+j] :
                            cpt += 1                # le cpt sert a compter si le symbole est égale a la où il doit être (je met 32 pour vérifier les 4 lignes et prendre moins de temps)
                            if cpt == 32 :           # si on retrouve le symbole en bas a droite on rotate
                                rotate(mat)
                        if k != mat[-8+i][-8+j] :
                            verifie = False

#création fenetre

###############################     pourquoi utiliser une interface ? on a pas besoin (on peut le faire en bonus mais apres afficher le résultat dedans c'est un peu plus chiant)

fenetre = tk.Tk()

canvas = tk.Canvas(fenetre, bg="black", height=HAUTEUR, width=LARGEUR)

bouton_charger = tk.Button(fenetre,text="charger",bg="blue",command=loading)

#positionnment widgets
canvas.grid()
bouton_charger.grid()



#lancement de la boucle
fenetre.mainloop()
