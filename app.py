#Importing tkinter and the files from the Scripts folder which was made into a package by adding
#an empty __init__.py file in it
from tkinter import *
from Scripts import caesar_cipher
from Scripts import shift_cipher
from Scripts import monoalphabetic_cipher
from Scripts import polyalphabetic_cipher
from Scripts import playfair_cipher
from Scripts import otp
from Scripts import hill_cipher
from Scripts import railfence
from Scripts import columnar
from Scripts import keyed_columnar_transposition_cipher

window = Tk()

window.mainloop()


