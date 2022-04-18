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


########################

# Variables globales



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


init_affichage(init_terrain())
root.mainloop()

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
