#Importing tkinter and the files from the Scripts folder which was made into a placeage by adding
#an empty __init__.py file in it
from functools import partial  
from tkinter import *
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
    global main_entry_plain
    global main_entry_key
    result.configure(text='')
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
    var = choice.get()
    if(var=='shift'):
        key = keyvalue.get()
        try:
            key = int(key)
        except Exception as e:
            output = 'Key needs to be an integer number between 1 and 25'
            result.configure(text=f'{output}')
            return
        if key<=0 or key>=26:
            output = 'Key needs to be an integer number between 1 and 25'
            result.configure(text=f'{output}')
            return    
        output = shift_cipher.shift_encipher(plaintext, key)
        result.configure(text=f'The ciphertext is {output}')
    elif(var=='caesar'):
        output = caesar_cipher.caesar_encipher(plaintext)
        result.configure(text=f'The ciphertext is {output}')
    elif(var=='monoalpha'):
        output = monoalphabetic_cipher.monoalphabetic_encipher(plaintext)
        result.configure(text=f'The cipher text is {output}')
    elif(var=='polyalpha'):
        key = keyvalue.get()
        key = key.upper()
        plaintext = plaintext.upper()
        parse=''
        for element in key:
            if element not in atoz and  element not in ATOZ:
                output = 'Key can have only alphabetical characters'
                result.configure(text=f'{output}')
                return
            else:
                parse+=element        
        key = parse
        if key=='' or len(key)<=0:
            output = 'No key entered or key is too small'
            result.configure(text=f'{output}')
            return             
        output = polyalphabetic_cipher.polyalphabetic_encipher(plaintext,key.upper()).lower()
        result.configure(text=f'The cipher text is {output}')
        return
    elif (var=='playfair'):
        key = keyvalue.get()
        plaintext = plaintext
        parse=''
        for element in key:
            if element not in atoz and  element not in ATOZ and element!=' ':
                output = 'Key can have only alphabetical characters'
                result.configure(text=f'{output}')
                return
            else:
                parse+=element        
        key = parse
        if key=='' or len(key)<=0:
            output = 'No key entered or key is too small'
            result.configure(text=f'{output}')
            return
        output = playfair_cipher.playfair_encipher(plaintext,key)
        result.configure(text=f'The cipher text is {output}')
        return   
        pass
    elif(var=='otp'):
        output = otp.otp_encipher(plaintext)
        result.configure(text=f'The cipher text is {output}')
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
                result.configure(text=f'{output}')
                return
                
        key = new
        n = len(key)
        if(n<=1):
            output = 'Matrix must be a sqaure matrix, i.e contain nxn elements where N is a Natural Number 2 onward'
            result.configure(text=f'{output}')
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
            result.configure(text=f'The cipher text is {output}')
            return
        else:
            output = 'Matrix must be a sqaure matrix, i.e contain nxn elements where N is a Natural Number 2 onward'
            result.configure(text=f'{output}')
            return
    elif (var=='railfence'):
        plaintext = plaintext.lower()
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
            result.configure(text=f'{output}')
            return
        output = railfence.railfence_encipher(plaintext,key)
        new = ''
        for element in output:
            if element not in atoz:
                pass
            else:
                new += element
        output = new
        result.configure(text=f'The cipher text is {output}')
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
                result.configure(text=f'{output}')
                return
                
        key = new
        plaintext = plaintext.lower()
        parse=''
        for element in plaintext:
            if element not in atoz:
                pass
            else:
                parse += element
        plaintext = parse
        output = columnar.columnar_transposition_encipher(plaintext,key)
        result.configure(text=f'The cipher text is {output}')
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
                result.configure(text=f'{output}')
                return
                
        key = new
        plaintext = plaintext.lower()
        parse=''
        for element in plaintext:
            if element not in atoz:
                pass
            else:
                parse += element
        plaintext = parse
        output = keyed_columnar_transposition_cipher.keyed_columnar_transposition_encipher(plaintext,key)
        result.configure(text=f'The cipher text is {output}')
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
    ciphertext = plain.get()
    var = choice.get()
    if(var=='shift'):
        key = keyvalue.get()
        try:
            key = int(key)
        except Exception as e:
            output = 'Key needs to be an integer number between 1 and 25'
            result.configure(text=f'{output}')
            return
        if key<=0 or key>=26:
            output = 'Key needs to be an integer number between 1 and 25'
            result.configure(text=f'{output}')
            return    
        output = shift_cipher.shift_decipher(ciphertext, key)
        result.configure(text=f'The ciphertext is {output}')
    elif(var=='caesar'):
        output = caesar_cipher.caesar_decipher(ciphertext)
        result.configure(text=f'The ciphertext is {output}')
    elif(var=='monoalpha'):
        output = monoalphabetic_cipher.monoalphabetic_decipher(ciphertext)
        output = output.lower()
        result.configure(text=f'The cipher text is {output}')
    elif(var=='polyalpha'):
        key = keyvalue.get()
        key = key.upper()
        ciphertext = ciphertext.upper()
        parse=''
        for element in key:
            if element not in atoz and  element not in ATOZ:
                output = 'Key can have only alphabetical characters'
                result.configure(text=f'{output}')
                return
            else:
                parse+=element        
        key = parse
        if key=='' or len(key)<=0:
            output = 'No key entered or key is too small'
            result.configure(text=f'{output}')
            return             
        output = polyalphabetic_cipher.polyalphabetic_decipher(ciphertext.upper(),key.upper()).lower()
        result.configure(text=f'The cipher text is {output}')
        return
    elif (var=='playfair'):
        key = keyvalue.get()
        ciphertext = ciphertext
        parse=''
        for element in key:
            if element not in atoz and  element not in ATOZ and element!=' ':
                output = 'Key can have only alphabetical characters'
                result.configure(text=f'{output}')
                return
            else:
                parse+=element        
        key = parse
        if key=='' or len(key)<=0:
            output = 'No key entered or key is too small'
            result.configure(text=f'{output}')
            return
        output = playfair_cipher.playfair_decipher(ciphertext,key)
        result.configure(text=f'The cipher text is {output}')
        return   
        pass
    elif(var=='otp'):
        output = otp.otp_encipher(ciphertext)
        result.configure(text=f'The cipher text is {output}')
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
                result.configure(text=f'{output}')
                return
                
        key = new
        n = len(key)
        if(n<=1):
            output = 'Matrix must be a sqaure matrix, i.e contain nxn elements where N is a Natural Number 2 onward'
            result.configure(text=f'{output}')
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
            result.configure(text=f'The cipher text is {output}')
            return
        else:
            output = 'Matrix must be a sqaure matrix, i.e contain nxn elements where N is a Natural Number 2 onward'
            result.configure(text=f'{output}')
            return
    elif (var=='railfence'):
        ciphertext = ciphertext.lower()
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
            result.configure(text=f'{output}')
            return
        output = railfence.railfence_decipher(ciphertext,key)
        new = ''
        for element in output:
            if element not in atoz:
                pass
            else:
                new += element
        output = new
        result.configure(text=f'The cipher text is {output}')
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
                result.configure(text=f'{output}')
                return
                
        key = new
        ciphertext = ciphertext.lower()
        parse=''
        for element in ciphertext:
            if element not in atoz:
                pass
            else:
                parse += element
        ciphertext = parse
        output = columnar.columnar_transposition_decipher(ciphertext,key)
        output = output.lower()
        result.configure(text=f'The cipher text is {output}')
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
                result.configure(text=f'{output}')
                return
                
        key = new
        ciphertext = ciphertext.lower()
        parse=''
        for element in ciphertext:
            if element not in atoz:
                pass
            else:
                parse += element
        ciphertext = parse
        output = keyed_columnar_transposition_cipher.keyed_columnar_transposition_decipher(ciphertext,key)
        output = output.lower()
        result.configure(text=f'The cipher text is {output}')
        return
    else:
        pass
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
window.configure(bg="#9992ff")
dropdown = OptionMenu(window, choice, *options)
dropdown.place(relx = 0.45, rely = 0.35, relwidth=0.1, relheight=0.1)
clear_window_text = Button(window,text="Clear", command = clearscreen)
clear_window_text.place(relx=0.85, rely = 0, relwidth=0.05, relheight=0.05)
exit_window = Button(window,text="Exit", command = window.destroy)
exit_window.place(relx=0.95, rely = 0, relwidth=0.05, relheight=0.05)
main_window_text = Label(window,text="Welcome to the Cipher Desktop Tool", font=("Helvetica", 22), bg="#9992ff")
main_window_text.place(relx=0.2, rely = 0, relwidth=0.6, relheight=0.2)
help_window_text = Button(window,text="Help", command = browser)
help_window_text.place(relx=0.9, rely = 0, relwidth=0.05, relheight=0.05)
result = Label(window, text='', font=("Helvetica", 22), bg="#9992ff" )
result.place(relx=0.1, rely = 0.2, relwidth=0.8, relheight=0.1)
main_entry_plain = Entry(window, textvariable=plain, width = 40)
main_entry_plain.place(relx = 0.1, rely = 0.3, relwidth = 0.3, relheight = 0.2)
main_entry_key = Entry(window, textvariable=keyvalue, width = 40)
main_entry_key.place(relx = 0.6, rely = 0.3, relwidth = 0.3, relheight = 0.2)
plaintext = Label(window,text='Enter the plaintext', bg="#9992ff", font=('Helvetice',12))
plaintext.place(relx = 0.14, rely = 0.5, relwidth = 0.2, relheight = 0.1)
key = Label(window,text='Enter the key', bg="#9992ff", font=('Helvetica',12))
key.place(relx = 0.55, rely = 0.5, relwidth = 0.4, relheight = 0.1)
main_enter_encipher = Button(window, text='Encipher', command = call_encipher)
main_enter_encipher.place(relx = 0.3, rely = 0.7, relwidth = 0.2, relheight = 0.2)
main_enter_decipher = Button(window, text='Decipher', command = call_decipher)
main_enter_decipher.place(relx = 0.5, rely = 0.7, relwidth = 0.2, relheight = 0.2)
window.mainloop()





