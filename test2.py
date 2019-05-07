from tkinter import *
fenetre = Tk()
# On définit la fonction appelée par le bouton
def valider():
 print ("Bonjour "+maZone.get())
# On crée un Label
champLabel = Label(fenetre, text="Nom : ")
champLabel.pack()
# On crée un Entry
maZone = Entry(fenetre, width=30)
maZone.insert(0, "Entrez votre nom ")
maZone.pack()
# On crée un Button
monBouton = Button(fenetre, text="Valider", command=valider)
# On affiche le Button dans la fenêtre
monBouton.pack() 