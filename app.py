#Importing tkinter and the files from the Scripts folder which was made into a placeage by adding
#an empty __init__.py file in it
from functools import partial  
from tkinter import *
import tkinter as tk
from tkinter import ttk
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
import string
import numpy as np
import math
import webbrowser


def browser():
    link = "help.pdf"
    webbrowser.open(link)


def clearscreen():
    global result
    global dropdown
    global main_entry_plain
    global main_entry_key
    choice.set('shift')
    result.configure(state='normal')
    result.delete(0,END)
    result.insert(0,'')
    main_entry_plain.delete(0, 'end')
    main_entry_key.delete(0, 'end')
    
        
def call_encipher():
    atoz = string.ascii_lowercase
    ATOZ = string.ascii_uppercase
    global choice
    global result
    global options
    global plain 
    global keyvalue
    output = ''
    plaintext = plain.get()
    parse=''
    for element in plaintext:
        if element==' ':
            pass
        else:
            parse += element
    plaintext = parse
    parse = ''
    for element in plaintext:
            if element not in atoz and  element not in ATOZ:
                output = 'Plaintext can have only alphabetical characters'
                result.configure(state='normal')
                result.delete(0,END) 
                result.insert(0,output)
                result.configure(state='readonly',bg="#63b8ff")
                return   
    var = choice.get()
    if(var=='shift'):
        key = keyvalue.get()
        try:
            key = int(key)
        except Exception as e:
            output = 'Key needs to be an integer number between 1 and 25'
            result.configure(state='normal')
            result.delete(0,END)
            result.insert(0,output)
            result.configure(state='readonly',bg="#63b8ff")
            return
        if key<=0 or key>=26:
            output = 'Key needs to be an integer number between 1 and 25'
            result.configure(state='normal')
            result.delete(0,END) 
            result.insert(0,output)
            result.configure(state='readonly',bg="#63b8ff")
            return    
        output = shift_cipher.shift_encipher(plaintext, key)
        output = f'The ciphertext is {output}'
        result.configure(state='normal')
        result.delete(0,END) 
        result.insert(0,output)
        result.configure(state='readonly',bg="#63b8ff")
    elif(var=='caesar'):
        output = caesar_cipher.caesar_encipher(plaintext)
        output = f'The ciphertext is {output}'
        result.configure(state='normal')
        result.delete(0,END) 
        result.insert(0,output)
        result.configure(state='readonly',bg="#63b8ff")
    elif(var=='monoalpha'):
        output = monoalphabetic_cipher.monoalphabetic_encipher(plaintext)
        output = f'The ciphertext is {output}'
        result.configure(state='normal')
        result.delete(0,END) 
        result.insert(0,output)
        result.configure(state='readonly',bg="#63b8ff")
    elif(var=='polyalpha'):
        key = keyvalue.get()
        if (len(plaintext)<len(key)):
            output = 'Key has to be lesser than or equal to plaintext in length'
            result.configure(state='normal')
            result.delete(0,END) 
            result.insert(0,output)
            result.configure(state='readonly',bg="#63b8ff")
            return
        key = key.upper()
        plaintext = plaintext.upper()
        parse=''
        for element in key:
            if element not in atoz and  element not in ATOZ:
                output = 'Key can have only alphabetical characters'
                result.configure(state='normal')
                result.delete(0,END) 
                result.insert(0,output)
                result.configure(state='readonly',bg="#63b8ff")
                return
            else:
                parse+=element        
        key = parse
        if key=='' or len(key)<=0:
            output = 'No key entered or key is too small'
            result.configure(state='normal')
            result.delete(0,END) 
            result.insert(0,output)
            result.configure(state='readonly',bg="#63b8ff")
            return             
        output = polyalphabetic_cipher.polyalphabetic_encipher(plaintext,key.upper()).lower()
        output = f'The ciphertext is {output}'
        result.configure(state='normal')
        result.delete(0,END) 
        result.insert(0,output)
        result.configure(state='readonly',bg="#63b8ff")
        return
    elif (var=='playfair'):
        key = keyvalue.get()
        plaintext = plaintext
        parse=''
        for element in key:
            if element not in atoz and  element not in ATOZ and element!=' ':
                output = 'Key can have only alphabetical characters'
                result.configure(state='normal')
                result.delete(0,END) 
                result.insert(0,output)
                result.configure(state='readonly',bg="#63b8ff")
                return
            else:
                parse+=element        
        key = parse
        if key=='' or len(key)<=0:
            output = 'No key entered or key is too small'
            result.configure(state='normal')
            result.delete(0,END) 
            result.insert(0,output)
            result.configure(state='readonly',bg="#63b8ff")
            return
        output = playfair_cipher.playfair_encipher(plaintext,key)
        output = f'The ciphertext is {output}'
        result.configure(state='normal')
        result.delete(0,END) 
        result.insert(0,output)
        result.configure(state='readonly',bg="#63b8ff")
        return   
        pass
    elif(var=='otp'):
        output = otp.otp_encipher(plaintext)
        output = f'The ciphertext is {output}'
        result.configure(state='normal')
        result.delete(0,END) 
        result.insert(0,output)
        result.configure(state='readonly',bg="#63b8ff")
        return
    elif(var=='hill'):
        plaintext = plaintext.lower()
        parse=''
        for element in plaintext:
            if element!=' ':
                parse+=element
            else:
                pass
        plaintext = parse
        parse = ''
        for element in plaintext:
            if element not in atoz and  element not in ATOZ:
                output = 'Plaintext can have only alphabetical characters'
                result.configure(state='normal')
                result.delete(0,END) 
                result.insert(0,output)
                result.configure(state='readonly',bg="#63b8ff")
                return
            else:
                parse+=element        
        plaintext = parse
        
        key = keyvalue.get()
        key = key.split(',')
        new = []
        for keys in key:
            try:
                new.append(int(keys))
            except Exception as e:
                output = 'Matrix must be a sqaure matrix, i.e contain nxn elements where N is a Natural Number'
                result.configure(state='normal')
                result.delete(0,END) 
                result.insert(0,output)
                result.configure(state='readonly',bg="#63b8ff")
                return
                
        key = new
        n = len(key)
        if(n<=1):
            output = 'Matrix must be a sqaure matrix, i.e contain nxn elements where N is a Natural Number 2 onward'
            output = f'The ciphertext is {output}'
            result.configure(state='normal')
            result.delete(0,END) 
            result.insert(0,output)
            result.configure(state='readonly',bg="#63b8ff")
            return
        if(math.ceil(math.sqrt(n)) == math.floor(math.sqrt(n))):
            size = math.ceil(math.sqrt(n))
            new = []
            for i in range(size):
                new.append([])
                for j in range(size):
                    new[i].append(key[size*i+j])
            key = new
            key = np.matrix(key)
            output = hill_cipher.hill_encipher(plaintext,key)
            output = f'The ciphertext is {output}'
            result.configure(state='normal')
            result.delete(0,END) 
            result.insert(0,output)
            result.configure(state='readonly',bg="#63b8ff")
            return
        else:
            output = 'Matrix must be a sqaure matrix, i.e contain nxn elements where N is a Natural Number 2 onward'
            result.configure(state='normal')
            result.delete(0,END) 
            result.insert(0,output)
            result.configure(state='readonly',bg="#63b8ff")
            return
    elif (var=='railfence'):
        plaintext = plaintext.lower()
        parse=''
        for element in plaintext:
            if element not in atoz and  element not in ATOZ:
                output = 'Plaintext can have only alphabetical characters'
                result.configure(state='normal')
                result.delete(0,END) 
                result.insert(0,output)
                result.configure(state='readonly',bg="#63b8ff")
                return
            else:
                parse+=element        
        plaintext = parse

        new = ''
        for element in plaintext:
            if element not in atoz:
                pass
            else:
                new += element
        plaintext = new
        key = keyvalue.get()
        try:
            key = int(key)
        except Exception as e:
            output = 'Key needs to be an integer number'
            result.configure(state='normal')
            result.delete(0,END)
            result.insert(0,output)
            result.configure(state='readonly',bg="#63b8ff")
            return
        output = railfence.railfence_encipher(plaintext,key)
        new = ''
        for element in output:
            if element not in atoz:
                pass
            else:
                new += element
        output = new
        output = f'The ciphertext is {output}'
        result.configure(state='normal')
        result.delete(0,END)
        result.insert(0,output)
        result.configure(state='readonly',bg="#63b8ff")
        return
    elif (var=='columnar'):
        key = keyvalue.get()
        key = key.split(',')
        new = []
        for keys in key:
            try:
                new.append(int(keys))
            except Exception as e:
                output = 'Enter a list of numbers between 1 and n in any order of size n'
                result.configure(state='normal')
                result.delete(0,END)
                result.insert(0,output)
                result.configure(state='readonly',bg="#63b8ff")
                return
                
        key = new
        plaintext = plaintext.lower()
        parse=''
        for element in plaintext:
            if element not in atoz and  element not in ATOZ:
                output = 'Plaintext can have only alphabetical characters'
                result.configure(state='normal')
                result.delete(0,END) 
                result.insert(0,output)
                result.configure(state='readonly',bg="#63b8ff")
                return
            else:
                parse+=element        
        plaintext = parse
        parse=''
        for element in plaintext:
            if element not in atoz:
                pass
            else:
                parse += element
        plaintext = parse
        output = columnar.columnar_transposition_encipher(plaintext,key)
        output = f'The ciphertext is {output}'
        result.configure(state='normal')
        result.delete(0,END)
        result.insert(0,output)
        result.configure(state='readonly',bg="#63b8ff")
        return
    elif (var=='keycolumnar'):
        key = keyvalue.get()
        key = key.split(',')
        new = []
        for keys in key:
            try:
                new.append(int(keys))
            except Exception as e:
                output = 'Enter a list of numbers between 1 and n in any order of size n'
                result.configure(state='normal')
                result.delete(0,END)
                result.insert(0,output)
                result.configure(state='readonly',bg="#63b8ff")
                return
                
        key = new
        plaintext = plaintext.lower()
        parse=''
        for element in plaintext:
            if element not in atoz and  element not in ATOZ:
                output = 'Plaintext can have only alphabetical characters'
                result.configure(state='normal')
                result.delete(0,END) 
                result.insert(0,output)
                result.configure(state='readonly',bg="#63b8ff")
                return
            else:
                parse+=element        
        plaintext = parse
        parse=''
        for element in plaintext:
            if element not in atoz:
                pass
            else:
                parse += element
        plaintext = parse
        output = keyed_columnar_transposition_cipher.keyed_columnar_transposition_encipher(plaintext,key)
        output = f'The ciphertext is {output}'
        result.configure(state='normal')
        result.delete(0,END)
        result.insert(0,output)
        result.configure(state='readonly',bg="#63b8ff")
        return
    else:
        pass
def call_decipher():
    atoz = string.ascii_lowercase
    ATOZ = string.ascii_uppercase
    global choice
    global result
    global options
    global plain 
    global keyvalue
    output = ''
    ciphertext = plain.get().lower()
    parse=''
    for element in ciphertext:
        if element==' ':
            pass
        else:
            parse += element
    ciphertext = parse
    parse = ''
    var = choice.get()
    if(var!='otp'):
        for element in ciphertext:
                if element not in atoz and  element not in ATOZ:
                    output = 'Ciphertext can have only alphabetical characters'
                    result.configure(state='normal')
                    result.delete(0,END) 
                    result.insert(0,output)
                    result.configure(state='readonly',bg="#63b8ff")
                    return  
    else:
        pass
    if(var=='shift'):
        key = keyvalue.get()
        try:
            key = int(key)
        except Exception as e:
            output = 'Key needs to be an integer number between 1 and 25'
            result.configure(state='normal')
            result.delete(0,END)
            result.insert(0,output)
            result.configure(state='readonly',bg="#63b8ff")
            return
        if key<=0 or key>=26:
            output = 'Key needs to be an integer number between 1 and 25'
            result.configure(state='normal')
            result.delete(0,END) 
            result.insert(0,output)
            result.configure(state='readonly',bg="#63b8ff")
            return    
        output = shift_cipher.shift_decipher(ciphertext, key).lower()
        output = f'The plaintext is {output}'
        result.configure(state='normal')
        result.delete(0,END) 
        result.insert(0,output)
        result.configure(state='readonly',bg="#63b8ff")
    elif(var=='caesar'):
        output = caesar_cipher.caesar_decipher(ciphertext)
        output = f'The plaintext is {output}'
        result.configure(state='normal')
        result.delete(0,END) 
        result.insert(0,output)
        result.configure(state='readonly',bg="#63b8ff")
    elif(var=='monoalpha'):
        output = monoalphabetic_cipher.monoalphabetic_decipher(ciphertext)
        output = f'The plaintext is {output}'
        result.configure(state='normal')
        result.delete(0,END) 
        result.insert(0,output)
        result.configure(state='readonly',bg="#63b8ff")
    elif(var=='polyalpha'):
        key = keyvalue.get()
        if (len(ciphertext)<len(key)):
            output = 'Key has to be lesser than or equal to ciphertext in length'
            result.configure(state='normal')
            result.delete(0,END) 
            result.insert(0,output)
            result.configure(state='readonly',bg="#63b8ff")
            return
        key = key.upper()
        parse=''
        for element in key:
            if element not in atoz and  element not in ATOZ:
                output = 'Key can have only alphabetical characters'
                result.configure(state='normal')
                result.delete(0,END) 
                result.insert(0,output)
                result.configure(state='readonly',bg="#63b8ff")
                return
            else:
                parse+=element        
        key = parse
        if key=='' or len(key)<=0:
            output = 'No key entered or key is too small'
            result.configure(state='normal')
            result.delete(0,END) 
            result.insert(0,output)
            result.configure(state='readonly',bg="#63b8ff")
            return             
        output = polyalphabetic_cipher.polyalphabetic_decipher(ciphertext.upper(),key.upper()).lower()
        output = f'The plaintext is {output}'
        result.configure(state='normal')
        result.delete(0,END) 
        result.insert(0,output)
        result.configure(state='readonly',bg="#63b8ff")
        return
    elif (var=='playfair'):
        key = keyvalue.get()
        key = key
        parse=''
        for element in key:
            if element not in atoz and  element not in ATOZ and element!=' ':
                output = 'Key can have only alphabetical characters'
                result.configure(state='normal')
                result.delete(0,END) 
                result.insert(0,output)
                result.configure(state='readonly',bg="#63b8ff")
                return
            else:
                parse+=element        
        key = parse
        if key=='' or len(key)<=0:
            output = 'No key entered or key is too small'
            result.configure(state='normal')
            result.delete(0,END) 
            result.insert(0,output)
            result.configure(state='readonly',bg="#63b8ff")
            return
        output = playfair_cipher.playfair_decipher(ciphertext,key)
        output = f'The plaintext is {output}'
        result.configure(state='normal')
        result.delete(0,END) 
        result.insert(0,output)
        result.configure(state='readonly',bg="#63b8ff")
        return   
        pass
    elif(var=='otp'):
        ciphertext = ciphertext.split(',')
        new = []
        for elements in ciphertext:
            try:
                new.append(int(elements))
            except Exception as e:
                output = 'Enter a list of numbers between 1 and n in any order of size n'
                result.configure(state='normal')
                result.delete(0,END)
                result.insert(0,output)
                result.configure(state='readonly',bg="#63b8ff")
                return
                
        ciphertext = new
        output = otp.otp_decipher(ciphertext).lower()
        output = f'The plaintext is {output}'
        result.configure(state='normal')
        result.delete(0,END) 
        result.insert(0,output)
        result.configure(state='readonly',bg="#63b8ff")
        return
    elif(var=='hill'):
        key = keyvalue.get()
        key = key.split(',')
        new = []
        for keys in key:
            try:
                new.append(int(keys))
            except Exception as e:
                output = 'Matrix must be a sqaure matrix, i.e contain nxn elements where N is a Natural Number'
                result.configure(state='normal')
                result.delete(0,END) 
                result.insert(0,output)
                result.configure(state='readonly',bg="#63b8ff")
                return
                
        key = new
        n = len(key)
        if(n<=1):
            output = 'Matrix must be a sqaure matrix, i.e contain nxn elements where N is a Natural Number 2 onward'
            output = f'The plaintext is {output}'
            result.configure(state='normal')
            result.delete(0,END) 
            result.insert(0,output)
            result.configure(state='readonly',bg="#63b8ff")
            return
        if(math.ceil(math.sqrt(n)) == math.floor(math.sqrt(n))):
            size = math.ceil(math.sqrt(n))
            new = []
            for i in range(size):
                new.append([])
                for j in range(size):
                    new[i].append(key[size*i+j])
            key = new
            key = np.matrix(key)
            output = hill_cipher.hill_decipher(ciphertext,key)
            output = f'The plaintext is {output}'
            result.configure(state='normal')
            result.delete(0,END) 
            result.insert(0,output)
            result.configure(state='readonly',bg="#63b8ff")
            return
        else:
            output = 'Matrix must be a sqaure matrix, i.e contain nxn elements where N is a Natural Number 2 onward'
            result.configure(state='normal')
            result.delete(0,END) 
            result.insert(0,output)
            result.configure(state='readonly',bg="#63b8ff")
            return
    elif (var=='railfence'):
        new = ''
        for element in ciphertext:
            if element not in atoz:
                pass
            else:
                new += element
        ciphertext = new
        key = keyvalue.get()
        try:
            key = int(key)
        except Exception as e:
            output = 'Key needs to be an integer number'
            result.configure(state='normal')
            result.delete(0,END)
            result.insert(0,output)
            result.configure(state='readonly',bg="#63b8ff")
            return
        output = railfence.railfence_decipher(ciphertext,key)
        new = ''
        for element in output:
            if element not in atoz:
                pass
            else:
                new += element
        output = new
        output = f'The plaintext is {output}'
        result.configure(state='normal')
        result.delete(0,END)
        result.insert(0,output)
        result.configure(state='readonly',bg="#63b8ff")
        return
    elif (var=='columnar'):
        key = keyvalue.get()
        key = key.split(',')
        new = []
        for keys in key:
            try:
                new.append(int(keys))
            except Exception as e:
                output = 'Enter a list of numbers between 1 and n in any order of size n'
                result.configure(state='normal')
                result.delete(0,END)
                result.insert(0,output)
                result.configure(state='readonly',bg="#63b8ff")
                return
                
        key = new
        
        parse=''
        for element in ciphertext:
            if element not in atoz:
                pass
            else:
                parse += element
        ciphertext = parse
        output = columnar.columnar_transposition_decipher(ciphertext,key)
        output = f'The plaintext is {output}'
        result.configure(state='normal')
        result.delete(0,END)
        result.insert(0,output)
        result.configure(state='readonly',bg="#63b8ff")
        return
    elif (var=='keycolumnar'):
        key = keyvalue.get()
        key = key.split(',')
        new = []
        for keys in key:
            try:
                new.append(int(keys))
            except Exception as e:
                output = 'Enter a list of numbers between 1 and n in any order of size n'
                result.configure(state='normal')
                result.delete(0,END)
                result.insert(0,output)
                result.configure(state='readonly',bg="#63b8ff")
                return
                
        key = new
        parse=''
        key = new
        parse=''
        for element in ciphertext:
            if element not in atoz and  element not in ATOZ:
                output = 'Plaintext can have only alphabetical characters'
                result.configure(state='normal')
                result.delete(0,END) 
                result.insert(0,output)
                result.configure(state='readonly',bg="#63b8ff")
                return
            else:
                parse+=element        
        ciphertext = parse
        parse=''
        for element in ciphertext:
            if element not in atoz:
                pass
            else:
                parse += element
        ciphertext = parse
        output = keyed_columnar_transposition_cipher.keyed_columnar_transposition_decipher(ciphertext,key)
        output = f'The plaintext is {output}'
        result.configure(state='normal')
        result.delete(0,END)
        result.insert(0,output)
        result.configure(state='readonly',bg="#63b8ff")
        return
    else:
        pass


#-Main Window-
window = Tk()
plain = StringVar()
keyvalue = StringVar()
choice = StringVar()
options = [
    'shift',
    'caesar',
    'monoalpha',
    'polyalpha',
    'playfair',
    'otp',
    'hill',
    'railfence',
    'columnar',
    'keycolumnar'    
]
choice.set('shift')
width= window.winfo_screenwidth()               
height= window.winfo_screenheight()               
window.geometry("%dx%d" % (width, height))
window.title('Cipher Desktop Application')
window.resizable('false','false')
window.configure(bg="#63b8ff")
dropdown = OptionMenu(window, choice, *options)
dropdown.place(relx = 0.45, rely = 0.35, relwidth=0.1, relheight=0.1)
clear_window_text = Button(window,text="Clear", command = clearscreen)
clear_window_text.place(relx=0.85, rely = 0, relwidth=0.05, relheight=0.05)
exit_window = Button(window,text="Exit", command = window.destroy)
exit_window.place(relx=0.95, rely = 0, relwidth=0.05, relheight=0.05)
logo = tk.PhotoImage(file='images/logo.png')
logo_display = Text(window, bg="#63b8ff")
logo_display.image_create(END,image = logo)
logo_display.place(relx=0.05, rely = 0.05, relwidth=0.06, relheight=0.1)
main_window_text0 = Label(window,text="Cryptography Mini Project",fg='#5f0f40', font=("Helvetica", 28), bg="#63b8ff")
main_window_text0.place(relx=0.2, rely = 0, relwidth=0.6, relheight=0.05)
main_window_textname0 = Label(window,text="Nobin Johnson ENG18CS0197",fg='#5f0f40', font=("Helvetica", 12), bg="#63b8ff")
main_window_textname0.place(relx=0.2, rely = 0.1, relwidth=0.6, relheight=0.05)
main_window_textname1= Label(window,text="Rahul Noronha ENG18CS0222",fg='#5f0f40', font=("Helvetica", 12), bg="#63b8ff")
main_window_textname1.place(relx=0.2, rely = 0.15, relwidth=0.6, relheight=0.05)
main_window_text = Label(window,text="Welcome to the Cipher Desktop Tool!",fg='#5f0f40', font=("Helvetica", 22), bg="#63b8ff")
main_window_text.place(relx=0.2, rely = 0.05, relwidth=0.6, relheight=0.05)
help_window_text = Button(window,text="Help", command = browser)
help_window_text.place(relx=0.9, rely = 0, relwidth=0.05, relheight=0.05)
result = Entry(window, bd=0, font=("Helvetica", 22), bg="#63b8ff" )
result.place(relx=0.1, rely = 0.2, relwidth=0.8, relheight=0.1)
main_entry_plain = Entry(window, textvariable=plain, width = 40)
main_entry_plain.place(relx = 0.1, rely = 0.3, relwidth = 0.3, relheight = 0.2)
main_entry_key = Entry(window, textvariable=keyvalue, width = 40)
main_entry_key.place(relx = 0.6, rely = 0.3, relwidth = 0.3, relheight = 0.2)
plaintext = Label(window,text='Enter the plaintext/ciphertext',fg='#5f0f40', bg="#63b8ff", font=('Helvetice',12))
plaintext.place(relx = 0.14, rely = 0.5, relwidth = 0.2, relheight = 0.1)
key = Label(window,text='Enter the key', fg='#5f0f40', bg="#63b8ff", font=('Helvetica',12))
key.place(relx = 0.55, rely = 0.5, relwidth = 0.4, relheight = 0.1)
main_enter_encipher = Button(window, text='Encipher', command = call_encipher)
main_enter_encipher.place(relx = 0.3, rely = 0.7, relwidth = 0.2, relheight = 0.2)
main_enter_decipher = Button(window, text='Decipher', command = call_decipher)
main_enter_decipher.place(relx = 0.5, rely = 0.7, relwidth = 0.2, relheight = 0.2)
window.mainloop()





