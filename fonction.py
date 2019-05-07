from Tkinter import *
from Tkinter import ttk
from Tkinter.messagebox import showinfo
import psycopg2
import psycopg2.extras
import sys
import pprint
import re

class Fonction:
    def Connexion(self):
        try:
            conn = psycopg2.connect(host="localhost", user="openpg", password="openpgpwd", database="dev")
            cursor = conn.cursor()

            cursor.execute('Select *From club')
            conn.commit()

        except psycopg2.databaseError as e:
            if conn:
                conn.rollback()
            print ('Error %s' % e)
            sys.exit(1)
        finally:
            if conn:
                conn.close()

    def Select(self):

        Connexion()
        while True:
            row = cursor.fetchone()

            if  row == None:
                break
            self.tree.insert('',0,text=row[1],values=row[2])

    def Ajouter(self):


    def Supprimer(Self):


    def Modifier(self):


    def Edite_Modif(self):
