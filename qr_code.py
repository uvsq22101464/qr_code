# PROJET QRCODE DONT LE BUT EST DE DECODER UN QRCODE

# MACHE Ethan
# BARBOSA Sam
# https://github.com/uvsq22101464/qr_code

# importation de librairies

import tkinter as tk
import PIL as pil
from PIL import Image
from tkinter import filedialog

# fonctions


def nbrCol(matrice):
    return(len(matrice[0]))


def nbrLig(matrice):
    return len(matrice)


def saving(matPix, filename):
    toSave = pil.Image.new(mode="1", size=(nbrCol(matPix), nbrLig(matPix)))
    for i in range(nbrLig(matPix)):
        for j in range(nbrCol(matPix)):
            toSave.putpixel((j, i), matPix[i][j])
    toSave.save(filename)


def loading(filename):
    """charge le fichier image filename et renvoie une matrice \
         de 0 (noir) et de 1 (blanc)"""
    global mat
    toLoad = pil.Image.open(filename)
    mat = [[0]*toLoad.size[0] for k in range(toLoad.size[1])]
    mat_modif = [[0]*toLoad.size[0] for k in range(toLoad.size[1])]
    for i in range(toLoad.size[1]):
        for j in range(toLoad.size[0]):
            mat[i][j] = 0 if toLoad.getpixel((j, i)) == 0 else 1
    return mat, mat_modif


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
        for j in range(25 - 1, -1, -1):  # j va de -1 a -25
            tempo.append(mat[j][i])  # on recopie la colonne i sur la ligne i
        mat_tempo.append(tempo)  # on l'ajoute dans une matrice temporaire
    for i in range(25):
        for j in range(25):
            mat[i][j] = mat_tempo[i][j]  # on réécrit la matrice
    return mat


def verify(mat):
    """vérifie si la matrice est dans le bon sens"""
    verifie = True
    while verifie:
        for i in range(len(symbole)):
            for j in range(len(symbole)):
                for k in symbole[i]:
                    if k == mat[17+i][17+j]:
                        verifie = True
                    else:
                        rotate(mat)
                        verifie = False


def verify_horizontale(mat):
    """vérifie si la ligne horizontale entre les symboles est bien présente"""
    verify = 0
    if mat[6] == [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0]:
        # compare la ligne 6 à la ligne qui doit etre présente renvoie vrai ou faux
        verify = True
        print("il y a bien la ligne horizontale")
    else:
        verify = False
        print("il n'y a pas la ligne horizontale")
    return verify


def verify_verticale(mat):
    """vérifie si la ligne verticale entre les symboles est bien présente"""
    global mat_temporaire
    verify = 0
    mat_temporaire = []
    for i in range(7, 18):
        mat_temporaire.append(mat[i][6])  # il faut ajouter les éléments de la colonne mat dans une autre liste

    if mat_temporaire == [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]:  # compare la colonne 7 à la ligne qui doit etre présente renvoie true ou false
        verify = True
        print("il y a bien la ligne verticale")
    else:
        verify = False
        print("il n'y a pas la ligne verticale")
    return verify


def correcteur(l):
    """Cherche une erreur et corrige l'erreur si il y en a une"""
    b1, b2, b3, b4, b5, b6, b7, b8 = l[0][0], l[0][1], l[0][2], l[0][3], l[0][7], l[0][8], l[0][9], l[0][10]
    p1, p2, p3, p4, p5, p6 = l[0][4], l[0][5], l[0][6], l[0][11], l[0][12], l[0][13]
    if (b1 + b2 + b4) % 2 == p1 and (b1 + b3 + b4) % 2 == p2 and (b2 + b3 + b4) % 2 == p3 and (b5 + b6 + b8) % 2 == p4 and (b5 + b7 + b8) % 2 == p5 and (b6 + b7 + b8) % 2 == p6:
        return[b1, b2, b3, b4, p1, p2, p3, b5, b6, b7, b8, p4, p5, p6]
    else:
        if p1 != (b1 + b2 + b4) % 2 and p2 == (b1 + b3 + b4) % 2 and p3 == (b2 + b3 + b4) % 2:
            p1 = (b1 + b2 + b4) % 2
        if p1 == (b1 + b2 + b4) % 2 and p2 != (b1 + b3 + b4) % 2 and p3 == (b2 + b3 + b4) % 2:
            p2 = (b1 + b3 + b4) % 2
        if p1 == (b1 + b2 + b4) % 2 and p2 == (b1 + b3 + b4) % 2 and p3 != (b2 + b3 + b4) % 2:
            p3 = (b2 + b3 + b4) % 2
        if p1 != (b1 + b2 + b4) % 2 and p2 != (b1 + b3 + b4) % 2 and p3 == (b2 + b3 + b4) % 2:
            if b1 == 0:
                b1 = 1
            else:
                b1 = 0
        if p1 != (b1 + b2 + b4) % 2 and p2 == (b1 + b3 + b4) % 2 and p3 != (b2 + b3 + b4) % 2:
            if b2 == 0:
                b2 = 1
            else:
                b2 = 0
        if p1 == (b1 + b2 + b4) % 2 and p2 != (b1 + b3 + b4) % 2 and p3 != (b2 + b3 + b4) % 2:
            if b3 == 0:
                b3 = 1
            else:
                b3 = 0
        if p1 != (b1 + b2 + b4) % 2 and p2 != (b1 + b3 + b4) % 2 and p3 != (b2 + b3 + b4) % 2:
            if b4 == 0:
                b4 = 1
            else:
                b4 = 0
        if p4 != (b5 + b6 + b8) % 2 and p5 == (b5 + b7 + b8) % 2 and p6 == (b6 + b7 + b8) % 2:
            p4 = (b5 + b6 + b8) % 2
        if p4 == (b5 + b6 + b8) % 2 and p5 != (b5 + b7 + b8) % 2 and p6 == (b6 + b7 + b8) % 2:
            p5 = (b5 + b7 + b8) % 2
        if p4 == (b5 + b6 + b8) % 2 and p5 == (b5 + b7 + b8) % 2 and p6 != (b6 + b7 + b8) % 2:
            p6 = (b6 + b7 + b8) % 2
        if p4 != (b5 + b6 + b8) % 2 and p5 != (b5 + b7 + b8) % 2 and p6 == (b6 + b7 + b8) % 2:
            if b5 == 0:
                b5 = 1
            else:
                b5 = 0
        if p4 != (b5 + b6 + b8) % 2 and p5 == (b5 + b7 + b8) % 2 and p6 != (b6 + b7 + b8) % 2:
            if b6 == 0:
                b6 = 1
            else:
                b6 = 0
        if p4 == (b5 + b6 + b8) % 2 and p5 != (b5 + b7 + b8) % 2 and p6 != (b6 + b7 + b8) % 2:
            if b7 == 0:
                b7 = 1
            else:
                b7 = 0
        if p4 != (b5 + b6 + b8) % 2 and p5 != (b5 + b7 + b8) % 2 and p6 != (b6 + b7 + b8) % 2:
            if b8 == 0:
                b8 = 1
            else:
                b8 = 0
        print("erreur corriger")
        return[b1, b2, b3, b4, p1, p2, p3, b5, b6, b7, b8, p4, p5, p6]


def liste_info(matrice):
    """renvoi une liste de liste de bits de chaque bloc lu dans le bon sens"""
    global liste_bits
    liste_bits = []
    for y in range(12):
        if y % 2 == 0:
            for k in range(2):
                liste_bits.append([])
                if k == 0:
                    for i in range(1, 8):
                        for j in range(1, 3):
                            liste_bits[-1].append(matrice[-j-y*2][-i])
                else:
                    for i in range(8, 15):
                        for j in range(1, 3):
                            liste_bits[-1].append(matrice[-j-y*2][-i])
        else:
            for k in range(2):
                liste_bits.append([])
                if k == 1:
                    for i in range(18, 25):
                        for j in range(1, 3):
                            liste_bits[-1].append(matrice[-j-y*2][i])
                else:
                    for i in range(11, 18):
                        for j in range(1, 3):
                            liste_bits[-1].append(matrice[-j-y*2][i])
    return liste_bits


def nbr_bloc_decoder(mat):
    """La fonction permet de connaitre le nombre de bloc qu'il faudra décoder"""
    global res
    liste_nbr_bloc = []
    liste_nbr_bloc.append(mat[13][0])
    liste_nbr_bloc.append(mat[14][0])
    liste_nbr_bloc.append(mat[15][0])
    liste_nbr_bloc.append(mat[16][0])
    liste_nbr_bloc.append(mat[17][0])
    # convertir en base10
    res = 2**0 * liste_nbr_bloc[4] + 2**1 * liste_nbr_bloc[3] + 2**2 * liste_nbr_bloc[2] + 2**3 * liste_nbr_bloc[1] + 2**4 * liste_nbr_bloc[0]
    return res


def decoder(mat):
    """la fonction permet de decoder les blocs de 14 bits"""
    global liste_bits
    liste_dinfo = []
    liste_corriger = []
    mot = ""
    if mat[24][8] == 1:
        for i in range(res):
            liste_dinfo.append(liste_bits[i])
            liste_corriger.append(correcteur(liste_dinfo))
            carac = str(liste_corriger[0][0]) + str(liste_corriger[0][1]) + str(liste_corriger[0][2]) + str(liste_corriger[0][3]) \
                + str(liste_corriger[0][7]) + str(liste_corriger[0][8]) + str(liste_corriger[0][9]) + str(liste_corriger[0][10])
            cpt = 0
            for i in range(len(carac)):
                if int(carac[i]) == 0:
                    cpt += 0
                else:
                    cpt += 2**(len(carac)-1-i)
            mot += str(chr(cpt))
            liste_dinfo.remove(liste_dinfo[0])
            liste_corriger.remove(liste_corriger[0])
        return "le résultat du qr code est : " + mot
    elif mat[24][8] == 0:
        for i in range(0, res):
            liste_dinfo.append(liste_bits[i])
            liste_corriger.append(correcteur(liste_dinfo))
            carac1 = str(liste_corriger[0][0]) + str(liste_corriger[0][1]) + str(liste_corriger[0][2]) + str(liste_corriger[0][3])
            carac2 = str(liste_corriger[0][7]) + str(liste_corriger[0][8]) + str(liste_corriger[0][9]) + str(liste_corriger[0][10])
            cpt = 0
            for i in range(4):
                if int(carac1[i]) == 0:
                    cpt += 0
                else:
                    cpt += 2**(4-1-i)
            mot += str(cpt)
            mot += " "
            cpt = 0
            for i in range(4):
                if int(carac2[i]) == 0:
                    cpt += 0
                else:
                    cpt += 2**(4-1-i)
            mot += str(cpt)
            mot += " "
            liste_dinfo.remove(liste_dinfo[0])
            liste_corriger.remove(liste_corriger[0])
            trad_hexa(mot)
        return "le résultat du qr code est : " + nombre


def trad_hexa(nb):
    """traduit le nombre en base hexadécimale"""
    global nombre
    nombre = ""
    for i in nb.split():
        if int(i) == 10:
            nombre += "A"
        if int(i) == 11:
            nombre += "B"
        if int(i) == 12:
            nombre += "C"
        if int(i) == 13:
            nombre += "D"
        if int(i) == 14:
            nombre += "E"
        if int(i) == 15:
            nombre += "F"
        elif int(i) < 10:
            nombre += str(i)
    return nombre


def filtre(mat):
    """applique le filtre à la matrice du qr code"""
    global liste_bits
    if mat[22][8] == 0 and mat[23][8] == 0:
        return mat
    elif mat[22][8] == 0 and mat[23][8] == 1:  # damier
        print("filtre damier")
        noir = False
        for i in range(25):
            for j in range(25):
                if noir is False:
                    mat[i][j] = mat[i][j]
                else:
                    mat[i][j] = 1 ^ mat[i][j]
                noir = not noir
        return mat
    elif mat[22][8] == 1 and mat[23][8] == 0:  # lignes horizontales
        print("filtre ligne horizontale")
        noir = True
        for i in range(25):
            for j in range(25):
                if noir:
                    mat[i][j] = mat[i][j]
                else:
                    mat[i][j] = 1 ^ mat[i][j]
            noir = not noir
        return mat
    elif mat[22][8] == 1 and mat[23][8] == 1:  # lignes verticales
        print("filtre ligne verticale")
        noir = True
        for i in range(25):
            for j in range(25):
                if j % 2 == 1:
                    noir = False
                else:
                    noir = True
                if noir:
                    mat[i][j] = mat[i][j]
                else:
                    mat[i][j] = 1 ^ mat[i][j]
        return mat


loading(filename=filedialog.askopenfile(mode='rb', title='Choose a file'))
# ligne prise dans le TP4_photoshopCorrection IN 202

verify(mat)
print(verify_horizontale(mat))
print(verify_verticale(mat))
nbr_bloc_decoder(mat)
filtre(mat)
liste_info(mat)
print(decoder(mat))
