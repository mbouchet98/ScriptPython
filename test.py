from tkinter import *
from tkinter.messagebox import showinfo
fenetre = Tk()

#test = Label(fenetre, text='test')
#test.pack()

#bouton=Button(fenetre, text="Fermer", command=fenetre.quit)
#bouton.pack()


# tkinter pour lais des logiciel en python. c'est un mode fenetrer.
# sa y est je crois que j'adore python T-T .


def recupere():
    showinfo("Alerte", entree.get())

value = StringVar() 
value.set("Valeur")
entree = Entry(fenetre, textvariable=value, width=30)
entree.pack()

bouton = Button(fenetre, text="Valider", command=recupere)
bouton.pack()

fenetre.mainloop()
