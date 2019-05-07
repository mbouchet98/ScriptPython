#coding: utf-8

""" Création de programme fenêtré 

Tout est widget même la fenêtre

"""

import tkinter
# from tkinter import *

# Création de la fenêtre principale
mainapp = tkinter.Tk()

# Spécification d'un titre
mainapp.title("Mon premier programme")

# Taille minimale de la fenêtre
#mainapp.minsize(640, 480)

# Taille maximale de la fenêtre
#mainapp.maxsize(1280, 720)

# Interdire le redimensionnement
#mainapp.resizable(width=False, height=True)

# Position
#mainapp.positionfrom("user")

# Résolution de la fenêtre
# geometry("XxY+0+0")
# mainapp.geometry("800x600")
#mainapp.geometry("800x600+10+10")

"""
Centrer une fenêtre
position_X = (largeur_ecran // 2) - (largeur_fenêtre // 2)
position_Y = (hauteur_ecran // 2) - (hauteur_ecran // 2)
"""
largeur_ecran = mainapp.winfo_screenwidth()
hauteur_ecran = mainapp.winfo_screenheight()
largeur_fenêtre = 800
hauteur_fenêtre = 600
posX = (largeur_ecran // 2) - (largeur_fenêtre // 2)
posY = (hauteur_ecran // 2) - (hauteur_fenêtre // 2)
geo = "{}x{}+{}+{}".format(largeur_fenêtre, hauteur_fenêtre, posX, posY)
mainapp.geometry(geo)

# Execution de la fenêtre et garder celle ci ouverte
mainapp.mainloop()
# Autre méthode pour quitter la fenêtre -> mainapp.quit()