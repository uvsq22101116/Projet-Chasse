########################
# MITD-03
# Frédéric Li Combeau
# Lisa Vauvert
# Victor Combemorel
# Manel Mokrab
# https://github.com/uvsq-info/l1-python
########################

# Import des librairies

import tkinter as tk
import random as rd
from math import sqrt
import ast


########################

# Variables globales

HAUTEUR = 810
LARGEUR = 810
N = 30
PROIES = []
PREDATEURS = []
MIAM = 5

INTERRUPTION = False


#########################

# Fonctions

# Affichage

def init_affichage():
    """ Affiche la grille en paramètre dans un canvas tkinter """
    global HAUTEUR, LARGEUR, N, PROIES, PREDATEURS
    hauteur_case = HAUTEUR // N
    largeur_case = LARGEUR // N

    canvas.delete('all')
    for k in range(len(PROIES)):
        x = PROIES[k][-1][0]
        y = PROIES[k][-1][1]
        canvas.create_rectangle((x*largeur_case), (y*hauteur_case), (x*largeur_case+largeur_case), (y*hauteur_case+hauteur_case), fill="black")
    for l in range(len(PREDATEURS)):
        x = PREDATEURS[l][-1][0]
        y = PREDATEURS[l][-1][1]
        canvas.create_rectangle((x*largeur_case), (y*hauteur_case), (x*largeur_case+largeur_case), (y*hauteur_case+hauteur_case), fill="red")

# Création des proies et des prédateurs

def creer_proies(Apro=5, x=15, y=15):
    global PROIES 
    a = 0
    if len(PROIES) >= 1:
         a = PROIES[-1][0] + 1
    PROIES.append(a, Apro, [x,y])

def creer_n_proies(Npro=5):
    for i in range(Npro):
        x = rd.randint(0, 29) 
        y = rd.randint(0, 29) 
        creer_proies(x = x, y = y)

# Mouvements

def mouvement():
    deplacement_proies()
    deplacement_predateurs()
    init_affichage()
    manger()
    age()
    creer_n_proies(1)
    if len(PREDATEURS) == 0:
        return print("Les proies ont gagné !")
    elif len(PROIES) == 0:
        return print("Les prédateurs ont gagné !")
    elif INTERRUPTION == False:
        root.after(100, mouvement)

# Proies

def deplacement_proies():
    for i in range(len(PROIES)):
        # Vérification des cases libres
        nb = [0, 1, 2, 3, 4, 5, 6, 7]
        dir = rd.choice(nb)
        new_coords = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
        for j in range(8):
            if j == 0:
                x, y = PROIES[i][-1][0]-1, PROIES[i][-1][1]-1
            if j == 1:
                x, y = PROIES[i][-1][0], PROIES[i][-1][1]-1
            if j == 2:
                x, y = PROIES[i][-1][0]+1, PROIES[i][-1][1]-1
            if j == 3:
                x, y = PROIES[i][-1][0]-1, PROIES[i][-1][1]
            if j == 4:
                x, y = PROIES[i][-1][0]+1, PROIES[i][-1][1]
            if j == 5:
                x, y = PROIES[i][-1][0]-1, PROIES[i][-1][1]+1
            if j == 6:
                x, y = PROIES[i][-1][0], PROIES[i][-1][1]+1
            if j == 7:
                x, y = PROIES[i][-1][0]+1, PROIES[i][-1][1]+1
            if verif_cases(x, y) is False:
                nb.remove(j)
        # Déplacement
        if len(nb) == 0:
            return
        dir = rd.choice(nb)
        PROIES[i][-1][0], PROIES[i][-1][1] = PROIES[i][-1][0]+new_coords[dir][0], PROIES[i][-1][1]+new_coords[dir][1]

def verif_cases(x, y):
    if x <= 0 or x >= 29 or y <= 0 or y >= 29:
        return False
    for i in range(len(PROIES)):
        if x == PROIES[i][-1][0] and y == PROIES[i][-1][1]:
            return False
    for j in range(len(PREDATEURS)):
        if x == PREDATEURS[j][-1][0] and y == PREDATEURS[j][-1][1]:
            return False
    return True

def age():
    i = 0
    while i < len(PROIES):
        if PROIES[i][-2] == 0:
            PROIES.remove(PROIES[i])
        else:
            PROIES[i][-2] -= 1
            i += 1

def reproduction_proie():
    for i in mat:
        for j in mat[i]:
            if mat[i][j]==mat[i][j-1]:
                rep(i,j,1)
            elif mat[i][j]==mat[i][j+1]:
                rep(i,j,2)
            elif mat[i][j]==mat[i-1][j-1]:
                rep(i,j,3)
            elif mat[i][j]==mat[i-1][j+1]:
                rep(i,j,4)
            elif mat[i][j]==mat[i-1][j]:
                rep(i,j,5)
            elif mat[i][j]==mat[i+1][j-1]:
                rep(i,j,6)
            elif mat[i][j]==mat[i+1][j+1]:
                rep(i,j,7)
            elif mat[i][j]==mat[i+1][j]:
                rep(i,j,8)
def rep(i,j,k):
    global mat
    global proie
    if k==1:
        a = random.randint(-2,1)
        b = random.randint(-1,1)
        while a == -2 or a == 1 and b == 0:
            a = random.randint(-2,1)
            b = random.randint(-1,1)
    if k == 2:
        a = random.randint(-1,2)
        b = random.randint(-1,1)
        while a == -1 or a == 2 and b == 0:
            a = random.randint(-1,2)
            b = random.randint(-1,1)
    if k == 5:
        a = random.randint(-1,1)
        b = random.randint(-2,1)
        while b == -2 or b == 1 and a == 0:
            a = random.randint(-1,1)
            b = random.randint(-2,1)
    if k == 8:
        a = random.randint(-1,1)
        b = random.randint(-1,2)
        while b == -1 or b == 2 and a == 0:
            a = random.randint(-1,1)
            b = random.randint(-1,2)
    if k==3:
        a = random.randint(-2,1)
        b = random.randint(-2,1)
        while (b == 1 and a == -2)or(b == - 2 and a == 1)or(b == 0 and a == 0)or(b == -1 and a == -1):
            a = random.randint(-2,1)
            b = random.randint(-2,1)
    if k == 4:
        a = random.randint(-2,1)
        b = random.randint(-1,2)
        while (b == -1 and a == -2)or(b == 2 and a == 1)or(b == 0 and a == 0)or(b == 1 and a == -1):
            a = random.randint(-2,1)
            b = random.randint(-1,2)
    if k == 6:
        a = random.randint(-1,2)
        b = random.randint(-2,1)
        while (b == -2 and a == -1)or(b == 1 and a == 2)or(b == 0 and a == 0)or(b == -1 and a == 1):
            a = random.randint(-1,2)
            b = random.randint(-2,1)
    if k == 7:
        a = random.randint(-1,2)
        b = random.randint(-1,2)
        while (b == 2 and a == -1)or(b == -1 and a == 2)or(b == 0 and a == 0)or(b == 1 and a == 1):
            a = random.randint(-1,2)
            b = random.randint(-1,2)
    mat[i+a][j+b]=1
    proie[i+a][j+b]=age_proie

# Prédateurs

def deplacement_predateurs():
    for i in range(len(PREDATEURS)):
        coords = PREDATEURS[i][-1]
        distance = 1000
        cible = []
        for j in range(len(PROIES)):
            distancetmp = sqrt((PREDATEURS[i][-1][0] - PROIES[j][-1][0])**2 + (PREDATEURS[i][-1][1] - PROIES[j][-1][1])**2)
            if distancetmp <= distance:
                distance = distancetmp
                cible = PROIES[j][-1]
            PREDATEURS[i][-2] = cible
        for k in range(len(PREDATEURS)):
            if PREDATEURS[k][-1] == coords and k != i:
                break
        mouvement_predateur(PREDATEURS[i])


def mouvement_predateur(pr):
    if pr[-1][0] > pr[-2][0] and pr[-1][1] > pr[-2][1]:
        pr[-1][0], pr[-1][1] = pr[-1][0]-1, pr[-1][1]-1
        for i in range(len(PREDATEURS)):
            if PREDATEURS[i][0] != pr[0] and PREDATEURS[i][-1] == pr[-1]:
                pr[-1][0], pr[-1][1] = pr[-1][0]+1, pr[-1][1]+1

    elif pr[-1][0] < pr[-2][0] and pr[-1][1] == pr[-2][1]:
        pr[-1][0], pr[-1][1] = pr[-1][0]+1, pr[-1][1]
        for i in range(len(PREDATEURS)):
            if PREDATEURS[i][0] != pr[0] and PREDATEURS[i][-1] == pr[-1]:
                pr[-1][0], pr[-1][1] = pr[-1][0]-1, pr[-1][1]

    elif pr[-1][0] > pr[-2][0] and pr[-1][1] < pr[-2][1]:
        pr[-1][0], pr[-1][1] = pr[-1][0]-1, pr[-1][1]+1
        for i in range(len(PREDATEURS)):
            if PREDATEURS[i][0] != pr[0] and PREDATEURS[i][-1] == pr[-1]:
                pr[-1][0], pr[-1][1] = pr[-1][0]+1, pr[-1][1]-1

    elif pr[-1][0] == pr[-2][0] and pr[-1][1] > pr[-2][1]:
        pr[-1][0], pr[-1][1] = pr[-1][0], pr[-1][1]-1
        for i in range(len(PREDATEURS)):
            if PREDATEURS[i][0] != pr[0] and PREDATEURS[i][-1] == pr[-1]:
                pr[-1][0], pr[-1][1] = pr[-1][0], pr[-1][1]+1

    elif pr[-1][0] == pr[-2][0] and pr[-1][1] < pr[-2][1]:
        pr[-1][0], pr[-1][1] = pr[-1][0], pr[-1][1]+1
        for i in range(len(PREDATEURS)):
            if PREDATEURS[i][0] != pr[0] and PREDATEURS[i][-1] == pr[-1]:
                pr[-1][0], pr[-1][1] = pr[-1][0], pr[-1][1]-1

    elif pr[-1][0] < pr[-2][0] and pr[-1][1] > pr[-2][1]:
        pr[-1][0], pr[-1][1] = pr[-1][0]+1, pr[-1][1]-1
        for i in range(len(PREDATEURS)):
            if PREDATEURS[i][0] != pr[0] and PREDATEURS[i][-1] == pr[-1]:
                pr[-1][0], pr[-1][1] = pr[-1][0]-1, pr[-1][1]+1

    elif pr[-1][0] > pr[-2][0] and pr[-1][1] == pr[-2][1]:
        pr[-1][0], pr[-1][1] = pr[-1][0]-1, pr[-1][1]
        for i in range(len(PREDATEURS)):
            if PREDATEURS[i][0] != pr[0] and PREDATEURS[i][-1] == pr[-1]:
                pr[-1][0], pr[-1][1] = pr[-1][0]+1, pr[-1][1]

    elif pr[-1][0] < pr[-2][0] and pr[-1][1] < pr[-2][1]:
        pr[-1][0], pr[-1][1] = pr[-1][0]+1, pr[-1][1]+1
        for i in range(len(PREDATEURS)):
            if PREDATEURS[i][0] != pr[0] and PREDATEURS[i][-1] == pr[-1]:
                pr[-1][0], pr[-1][1] = pr[-1][0]-1, pr[-1][1]-1

def manger():
    for i in range(len(PREDATEURS)):
        for j in range(len(PROIES)):
            if PREDATEURS[i][-1] == PROIES[j][-1]:
                PROIES.remove(PROIES[j])
                break

# Sauvegarde, chargement, interruption et reprise

#########################

# Partie principale

root = tk.Tk()
root.title("Génération de terrain")

canvas = tk.Canvas(root, height=HAUTEUR, width=LARGEUR)
canvas.grid(column=1, row=0, rowspan=9)

# Création des widgets

bouton_init = tk.Button(text="Initialisation", command=init_terrain)
bouton_init.grid(column=0, row=0)

bouton_init = tk.Button(text="Play", command=play)
bouton_init.grid(column=0, row=1)

bouton_int = tk.Button(text="Interrompre", command=interruption)
bouton_int.grid(column=0, row=7)
bouton_rep = tk.Button(text="Reprendre", command=reprendre)
bouton_rep.grid(column=0, row=8)


init_affichage()
root.mainloop()
