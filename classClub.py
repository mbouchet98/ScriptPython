from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
import tkinter as tk
import psycopg2
import psycopg2.extras
import sys
import pprint	
import re


class ClassClub:

	db_name = 'dev.db'

	# Constructeur.

	def __init__(self, windowsClub):


		self.windowsClub = windowsClub
		self.windowsClub.title('Club')

		# Code pour le text
		# title = Label(self.windowsClub, text='Inscription Des Clubs', foreground='red')
		# title.config(font=('courier', 20, 'bold', 'italic', 'underline'))
		# title.pack(padx=10, pady=10)

		# ou 

		frame = LabelFrame(self.windowsClub, text='Inscription Des Clubs', foreground='red')
		frame.grid(row=0,column=1)
		frame.config(font=('courier', 20, 'bold', 'italic', 'underline'))
		

		# code pour les inputs
		Label(frame, text='Nom Du Club : ',padx=10, pady=10).grid(row=1,column=1)
		self.name = Entry(frame)
		self.name.grid(row=1,column=2,padx=10, pady=10)

		# value = StringVar()
		# test = value.get()
		# entree = Entry(self.windowsClub, textvariable=value, width=30)
		# entree.config(font=(40))
		# entree.pack(padx=10, pady=10)

		# ou

		Label(frame, text='Nombre Adherant Max : ',padx=10, pady=10).grid(row=2,column=1)
		self.nbadhmax = Entry(frame)
		self.nbadhmax.grid(row=2,column=2,padx=10, pady=10)

		# ou

		# value2 = IntVar()
		# test2 = value2.get()
		# entree2 = Entry(self.windowsClub, textvariable=value2, width=30)
		# entree2.config(font=(40))
		# entree2.pack(padx=10, pady=10)

		# Code pour un button.

		ttk.Button(frame, text='Ajouter', command=self.Ajouter).grid(row=3,column=2,padx=10, pady=10)
		self.message = Label(text = '', foreground='red', padx=10, pady=10)
		self.message.grid(row=3,column=0)


		#button = Button(self.windowsClub, text="Quit", command = self.windowsClub.quit) # trouver la commad et le code qui enregistre les données dans la base.
		#button.config(font=(40))
		#button.pack(padx=10, pady=10)

		self.tree = ttk.Treeview(height = 10, column = 2)
		self.tree.grid(row = 4, column = 0, columnspan= 2)
		self.tree.heading('#0', text='Nom Du Club', anchor = W)
		self.tree.heading(2, text='Nombre Adherant Max', anchor=W)
		
		ttk.Button(text='Supprimer', command=self.Supprimer).grid(row=5,column=0,padx=10, pady=10)
		ttk.Button(text='Modifier', command=self.Modifier).grid(row=5,column=1,padx=10, pady=10)

		self.Select_Data()

	# Fonction et Procédure. (getter/setter)

	def Select_Data(self):
		try:
			conn = psycopg2.connect(host="localhost", user="openpg", password="openpgpwd", database="dev")
			cursor = conn.cursor()
			
			# Code Pour les requets SQL.
			
			cursor.execute('SELECT * FROM club')
			conn.commit()

			while True:
				row = cursor.fetchone()

				if row == None:
					break
				
				self.tree.insert('',0,text=row[1], values = row[2])

			# afficher les erreur.
	
		except psycopg2.DatabaseError as e:
			if conn:
				conn.rollback()

			print ('Error %s' % e)
			sys.exit(1)

			# on ferme la connection a la base.
		finally:
			if conn:
				conn.close()

	def Validation(self):
		return len(self.name.get()) != 0 and len(self.nbadhmax.get()) != 0

	def isValidName(self):
		return re.search(r'[A-z][A-z]',self.name.get())

	def isValidNumberAdkMax(self):
		return re.search(r'[0-9]',self.nbadhmax.get())


	def Ajouter(self):
		try:
			conn = psycopg2.connect(host="localhost", user="openpg", password="openpgpwd", database="dev")
			cursor = conn.cursor()
			
			if self.Validation() and self.isValidName() and self.isValidNumberAdkMax():

				cursor.execute("INSERT INTO club (nom_club, nbadhmax) VALUES (%s, %s)", (self.name.get(), self.nbadhmax.get()))
				conn.commit()

				self.message['text'] = format(self.name.get())+' a bien été Ajouter'
				# netoie les champs de saisie.
				self.name.delete(0, END)
				self.nbadhmax.delete(0, END)
			else:
				
				self.message['text']='Les champs doivent être remplis \n ou Nom non Valide \n Nombre Adherant max non Valide '
			
				


			self.Select_Data()

			# afficher les erreur.
	
		except psycopg2.DatabaseError as e:
			if conn:
				conn.rollback()

			print ('Error %s' % e)
			sys.exit(1)

			# on ferme la connection a la base.
		finally:
			if conn:
				conn.close()

	def Supprimer(self):
		try:
			conn = psycopg2.connect(host="localhost", user="openpg", password="openpgpwd", database="dev")
			cursor = conn.cursor()
			
			self.message['text'] = ''

			try:
				self.tree.item(self.tree.selection())['values'][0]
				self.message['text'] = ''
				name = self.tree.item(self.tree.selection())['text']
				cursor.execute("DELETE FROM club WHERE nom_club = (%s)",(name,))
				conn.commit()
				self.message['text'] = format(name)+' a bien été Supprimer'

			except IndexError as e:
				self.message['text'] ='s il vous plait selectionner un enregistrement'
			
			self.Select_Data()

			# afficher les erreur.
	
		except psycopg2.DatabaseError as e:
			if conn:
				conn.rollback()

			print ('Error %s' % e)
			sys.exit(1)

			# on ferme la connection a la base.
		finally:
			if conn:
				conn.close()

	def Modifier(self):
		try:
			conn = psycopg2.connect(host="localhost", user="openpg", password="openpgpwd", database="dev")
			cursor = conn.cursor()
			
			self.message['text'] = ''

			try:
				self.tree.item(self.tree.selection())['values'][0]
				
				name = self.tree.item(self.tree.selection())['text']
				nbadhmax = self.tree.item(self.tree.selection())['values'][0]

				self.edit_wind = Toplevel()
				self.edit_wind.title('Modifier un Club')

				Label(self.edit_wind, text='Nom Du Club : ').grid(row=0,column=1)
				Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=name), state='readonly').grid(row=0, column=2)
				Label(self.edit_wind, text='Nouveau nom de club : ').grid(row=1, column=1)
				new_name =Entry(self.edit_wind)
				new_name.grid(row=1, column=2)


				Label(self.edit_wind, text='Nombre Adherant Max : ').grid(row=2,column=1)
				Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=nbadhmax), state='readonly').grid(row=2, column=2)
				Label(self.edit_wind, text='Nouveau Nombre Adherant Max : ').grid(row=3, column=1)
				new_nbadhmax =Entry(self.edit_wind)
				new_nbadhmax.grid(row=3, column=2)

				ttk.Button(self.edit_wind, text='enregistrer', command=lambda:self.edit_records(new_name.get(), name, new_nbadhmax.get(), nbadhmax)).grid(row=4,column=2,sticky=W)

				self.edit_wind.mainloop()

			except IndexError as e:
				self.message['text'] ='s il vous plait selectionner un enregistrement'

			# afficher les erreur.
	
		except psycopg2.DatabaseError as e:
			if conn:
				conn.rollback()

			print ('Error %s' % e)
			sys.exit(1)

			# on ferme la connection a la base.
		finally:
			if conn:
				conn.close()

	def edit_records(self, new_name, name, new_nbadhmax, nbadhmax):
		
		try:
			conn = psycopg2.connect(host="localhost", user="openpg", password="openpgpwd", database="dev")
			cursor = conn.cursor()
			
			# Code Pour les requets SQL.
			
			cursor.execute("UPDATE club SET nom_club = %s, nbadhmax = %s WHERE nom_club = %s AND nbadhmax = %s",(new_name, new_nbadhmax, name, nbadhmax))
			conn.commit()

			self.message['text'] = format(name)+' a bien été Changer'
			self.Select_Data()

			# afficher les erreur.
	
		except psycopg2.DatabaseError as e:
			if conn:
				conn.rollback()

			print ('Error %s' % e)
			sys.exit(1)

			# on ferme la connection a la base.
		finally:
			if conn:
				conn.close()





# programe principal.

if __name__ == '__main__':

	# instanciation
	windowsClub = Tk()
	application = ClassClub(windowsClub)

	# fin de l'algo pp (pour pas que la fenetre se faire tout de suite)
	windowsClub.mainloop()