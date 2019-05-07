from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
import tkinter as tk
import psycopg2
import psycopg2.extras
import sys
import pprint
import re

# programe principal.
if __name__ == '__main__':

	# instanciation
	windowsClub = Tk()

	categorie1 = classCategorie()

	self.windowsClub = windowsClub
	self.windowsClub.title('Catégorie')

	frame = LabelFrame(self.windowsClub, text='Inscription Des Catégories', foreground='red')
	frame.grid(row=0,column=1)
	frame.config(font=('courier', 20, 'bold', 'italic', 'underline'))

	Label(frame, text='Nom De La Catégorie : ',padx=10, pady=10).grid(row=1,column=1)
	self.nom_cate = Entry(frame)
	self.nom_cate.grid(row=1,column=2,padx=10, pady=10)

	Label(frame, text='Nom Du Club : ',padx=10, pady=10).grid(row=2,column=1)
	self.nom_club = ttk.Treeview(frame,height = 10, column = 2)
	self.nom_club.grid(row=2,column=2,  columnspan= 2)
	self.nom_club.heading('#0', text='selectionner un club : ', anchor = W)
	self.nom_club.heading(2, text='Numéro Du Club : ', anchor=W)
	self.treeview = self.nom_club

	self.i = 0

	ttk.Button(frame, text='Ajouter', command=self.Ajouter).grid(row=3,column=2,padx=10, pady=10)
	self.message = Label(text = '', foreground='red', padx=10, pady=10)
	self.message.grid(row=3,column=0)

	self.tree = ttk.Treeview(windowsClub,height = 10, column = 2)
	self.tree.grid(row = 4, column = 0,columnspan= 2)
	self.tree.heading('#0', text='Nom De La Catégorie : ', anchor = W)
	self.tree.heading('#1', text='Nom Du Club : ', anchor=W)
	self.tree.heading('#2',text='Numéro Du Club : ', anchor=W)
	self.tree.column('#0', stretch=Tkinter.YES)
	self.tree.column('#1', stretch=Tkinter.YES)
	self.tree.column('#2', stretch=Tkinter.YES)

	ttk.Button(text='Supprimer', command=self.Supprimer).grid(row=5,column=0,padx=10, pady=10)
	ttk.Button(text='Modifier', command=self.Modifier).grid(row=5,column=1,padx=10, pady=10)

	self.Select_Data()
	self.Select()

	# fin de l'algo pp (pour pas que la fenetre se faire tout de suite)
	windowsClub.mainloop()
