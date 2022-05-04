#PROJET QRCODE DONT LE BUT EST DE DECODER UN QRCODE#




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
    global mat
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
    verifie = True
    while verifie == True :
        for i in range(len(symbole)) :
            for j in range(len(symbole)) :
                for k in symbole[i] :
                    if k == mat[17+i][17+j] :
                        verifie = True
                    else :
                        rotate(mat)
                        verifie = False




def verify_horizontale(mat):
    "vérifie si la ligne entre les symboles est bien présente"
    verify = 0
    if mat[7] ==  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0]:  #compare la ligne 7 à la ligne qui doit etre présente renvoie vrai ou faux
        verify = True
    else:
        verify = False
    return verify


def verify_verticale(mat):
    "vérifie si la ligne entre les symboles est bien présente"
    global mat_temporaire
    verify = 0

    mat_temporaire = []
    mat_temporaire.append(mat[8][7])
    mat_temporaire.append(mat[9][7])
    mat_temporaire.append(mat[10][7])
    mat_temporaire.append(mat[11][7])
    mat_temporaire.append(mat[12][7])
    mat_temporaire.append(mat[13][7])   #il faut ajouter les éléments de la colonne mat dans une autre liste
    
    if mat_temporaire ==  [0,0,0,0,0]:  #compare la colonne 7 à la ligne qui doit etre présente renvoie vrai ou false
        verify = True
    else:
        verify = False
    return verify

l =[]

def lecture_bits (mat): # pas nécesaire
    global l

    for i in range(nbrCol(mat)):
        for j in range(nbrLig(mat)):
            l = [mat[i][j],mat[i][j+1],mat[i][j+2],mat[i][j+3],mat[i][j+4],mat[i][j+5],mat[i][j+6]]
            return l


l = [1,0,1,0,0,1,0]

def decode(l): #decode hamming
    b1 = l[0]
    b2 = l[1]
    b3 = l[2]
    b4 = l[3]
    p1 = l[4]
    p2 = l[5]
    p3 = l[6]

    if ( b1 + b2 + b4) % 2 == p1 and ( b1 + b3 + b4) % 2 == p2 and ( b2 + b3 + b4) % 2 == p3:
        print("OK")
        return [b1,b2,b3,b4,p1,p2,p3]
    else:
        if p1 != ( b1 + b2 + b4) % 2 and p2 == ( b1 + b3 + b4) % 2 and p3 == ( b2 + b3 + b4) % 2:
            p1 = ( b1 + b2 + b4) % 2
        
        if p1 == ( b1 + b2 + b4) % 2 and p2 != ( b1 + b3 + b4) % 2 and p3 == ( b2 + b3 + b4) % 2:
            p2 = ( b1 + b3 + b4) % 2
        
        if p1 == ( b1 + b2 + b4) % 2 and p2 == ( b1 + b3 + b4) % 2 and p3 != ( b2 + b3 + b4) % 2:
            p3 = ( b2 + b3 + b4) % 2


        if p1 != ( b1 + b2 + b4) % 2 and p2 != ( b1 + b3 + b4) % 2:
             if b1 == 0:
                 b1 = 1
             else :
                b1 = 0
        if p1 != ( b1 + b2 + b4) % 2 and p3 != ( b2 + b3 + b4) % 2:
             if b2 == 0:
                 b2 = 1
             else :
                b2 = 0
        
        if p2 != ( b1 + b2 + b4) % 2 and p3 != ( b2 + b3 + b4) % 2:
             if b3 == 0:
                 b3 = 1
             else :
                b3 = 0
        
        if 1 != ( b1 + b2 + b4) % 2 and p2 != ( b1 + b2 + b4) % 2 and p3 != ( b2 + b3 + b4) % 2:
             if b4 == 0:
                 b4 = 1
             else :
                b4 = 0
             
             
        print("erreur corriger")


        return [b1,b2,b3,b4,p1,p2,p3]

def liste_info(matrice) :
    cpt = 0
    liste_bits = []
    for y in range(len(matrice)//2) :
        liste_bits.append([])
        for i in range(1, 8) :
            for j in range(1, 3) :
                liste_bits[y].append(matrice[-j-y*2][-i])
        cpt += 1
    return liste_bits



