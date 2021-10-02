#Importing tkinter and the files from the Scripts folder which was made into a placeage by adding
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

#-----------------------------------------------------Main Window------------------------------------------------------
window = Tk()
width= window.winfo_screenwidth()               
height= window.winfo_screenheight()               
window.geometry("%dx%d" % (width, height))
window.title('Cipher Desktop Application')
window.resizable('false','true')
window.minsize(width=width, height=300)
window.configure(bg="#f0f6fb")
main_window_text = Label(window,text="Welcome to the Cipher Desktop Tool", font=("Helvetica", 42), bg="#f0f6fb").place(relx=0.2, rely = 0.1, relwidth=0.6, relheight=0.2)
shift_button = Button(window, text="Shift Cipher", fg='black', bg='light gray').place(relheight=0.2, relwidth=0.15, relx = 0.02, rely = 0.4)
caesar_button = Button(window, text="Caesar Cipher", fg='black', bg='light gray').place(relheight=0.2, relwidth=0.15, relx = 0.22, rely = 0.4)
mono_button = Button(window, text="Monoalphabetic Cipher", fg='black', bg='light gray').place(relheight=0.2, relwidth=0.15, relx = 0.42, rely = 0.4)
poly_button = Button(window, text="Polyalphabetic Cipher", fg='black', bg='light gray').place(relheight=0.2, relwidth=0.15, relx = 0.62, rely = 0.4)
playfair_button = Button(window, text="Playfair Cipher", fg='black', bg='light gray').place(relheight=0.2, relwidth=0.15, relx = 0.82, rely = 0.4)
otp_button = Button(window, text="One Time Pad Cipher", fg='black', bg='light gray').place(relheight=0.2, relwidth=0.15, relx = 0.02, rely = 0.7)
hill_button = Button(window, text="Hill Cipher", fg='black', bg='light gray').place(relheight=0.2, relwidth=0.15, relx = 0.22, rely = 0.7)
railfence_button = Button(window, text="Railfence Cipher", fg='black', bg='light gray').place(relheight=0.2, relwidth=0.15, relx = 0.42, rely = 0.7)
col_transpos_button = Button(window, text="Columnar Transposition Cipher", fg='black', bg='light gray').place(relheight=0.2, relwidth=0.15, relx = 0.62, rely = 0.7)
key_col_transpos_button = Button(window, text="Keyed Columnar Transposition Cipher", fg='black', bg='light gray').place(relheight=0.2, relwidth=0.15, relx = 0.82, rely = 0.7)
window.mainloop()




