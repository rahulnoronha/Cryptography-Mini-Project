#The Playfair cipher or Playfair square or Wheatstone–Playfair cipher is a manual symmetric encryption technique and was 
# the first literal digram substitution cipher. The scheme was invented in 1854 by Charles Wheatstone, 
# but bears the name of Lord Playfair for promoting its use.

import string



def handle_odd_adjacent(plaintext):
    atoz = string.ascii_lowercase
    #Since i and j in the 5x5 matrix are represented in the same spot, let us replace j in atoz by .
    atoz = atoz.replace('j','.')
    store = ''
    for i in plaintext:
        if i in atoz:
            store+=i
        elif i=='j':
            store+='i'
        else:
            pass
    plaintext = store        
    #Handle two adjacent letter pairs being the same
    result_str = ""
    if(len(plaintext)%2==0):
        for i in range(0,len(plaintext),2):
            if(plaintext[i]==plaintext[i+1] and plaintext[i]!=" "):
                result_str += f'{plaintext[i]}x{plaintext[i+1]}'
            elif (plaintext[i]==" "):
                if(plaintext[i+1]==" "):
                    pass
                else:
                    result_str += plaintext[i+1]
            elif (plaintext[i+1]==" "):
                if(plaintext[i]==" "):
                    pass
                else:
                    result_str += plaintext[i]        
            else:
                result_str += f'{plaintext[i]}{plaintext[i+1]}'
        if(len(result_str)%2==0):
            pass
        else:
            result_str += 'x' 
        return result_str  
    else:
        for i in range(0,len(plaintext)-1,2):
            if(plaintext[i]==plaintext[i+1] and plaintext[i]!=" "):
                result_str += f'{plaintext[i]}x{plaintext[i+1]}'
            elif (plaintext[i]==" "):
                if(plaintext[i+1]==" "):
                    pass
                else:
                    result_str += plaintext[i+1]
            elif (plaintext[i+1]==" "):
                if(plaintext[i]==" "):
                    pass
                else:
                    result_str += plaintext[i]        
            else:
                result_str += f'{plaintext[i]}{plaintext[i+1]}'
        result_str += plaintext[-1]
        
        if(len(result_str)%2==0):
            pass
        else:                    
            result_str += 'x'         
        return result_str    

def playfair_encipher(plaintext,key):
    plaintext = plaintext.lower()
    key = key.lower()
    atoz = string.ascii_lowercase
    #Since i and j in the 5x5 matrix are represented in the same spot, let us replace j in atoz by .
    atoz = atoz.replace('j','.')
    #Rule 1
    '''
    If both letters are the same (or only one letter is left),
    add an "X" after the first letter. Encrypt the new 
    pair and continue. Some variants of Playfair use 
    "Q" instead of "X", but any letter, 
    itself uncommon as a repeated pair, will do.
    '''
    #Handle two adjacent letter pairs being the same
    #Handle odd number of letters being present
    new_plaintext = handle_odd_adjacent(plaintext)
    #Constructing 5x5 matrix of Playfair Cipher
    key_matrix = ['' for i in range(5)]
    row = 0
    col = 0
    for element in key:
        if element in atoz:
            key_matrix[row] += element
            atoz = atoz.replace(element,'.')
            col+=1
            if(col>4):
                row+=1
                col = 0
    for element in atoz:
        if element!='.':
            key_matrix[row]+=element
            col+=1
            if col>4:
                row+=1
                col = 0
                
    #Rule 2
    '''
    If the letters appear on the same row of your table, replace them with the letters to 
    their immediate right respectively (wrapping around to the left side of the 
    row if a letter in the original pair was on the right side of the row).
    '''
    #Rule 3
    '''
    If the letters appear on the same column of your table, replace them with the 
    letters immediately below respectively (wrapping around to the top side of the 
    column if a letter in the original pair was on the bottom side of the column).
    '''
    #Rule 4
    '''
    If the letters are not on the same row or column, replace them with the 
    letters on the same row respectively but at the other pair of corners of the rectangle defined 
    by the original pair. The order is important – the first letter of the encrypted pair is 
    the one that lies on the same row as the first letter of the plaintext pair.
    '''
    result_str = ''
    for i in range(0,len(new_plaintext),2):
        #Apply rule 2,3 or 4 for converting the plaintext to ciphertext
        pos0 = -1
        pos1 = -1
        pos2 = -1
        pos3 = -1
        for row in key_matrix:
            if((new_plaintext[i] in row) and (new_plaintext[i+1] in row)):
                pos0 = row.find(new_plaintext[i])
                pos1 = row.find(new_plaintext[i+1])
                result_str += row[(pos0+1)%5]
                result_str += row[(pos1+1)%5]
        if pos0!=-1 and pos1!=-1:
            continue
        element0 = ''
        element1 = ''
        for row in key_matrix:
            if(new_plaintext[i] in row): 
                pos2 = row.find(new_plaintext[i])
            if(new_plaintext[i+1] in row):
                pos3 = row.find(new_plaintext[i+1])
        if pos2!=pos3:
            for row in key_matrix:
                if(new_plaintext[i] in row):
                    element0 = row[pos3]
                if(new_plaintext[i+1] in row):
                    element1 = row[pos2]
            result_str += f'{element0}{element1}'
        
        else:
            for index, row in enumerate(key_matrix):
                if(new_plaintext[i] in row):
                    element0 = key_matrix[(index+1)%5][pos2]
                if(new_plaintext[i+1] in row):
                    element1 = key_matrix[(index+1)%5][pos3]
            result_str += f'{element0}{element1}'
    return result_str

def playfair_decipher(ciphertext,key):
    ciphertext = ciphertext.lower()
    key = key.lower()
    atoz = string.ascii_lowercase
    #Since i and j in the 5x5 matrix are represented in the same spot, let us replace j in atoz by .
    atoz = atoz.replace('j','.')
    #Constructing 5x5 matrix of Playfair Cipher
    key_matrix = ['' for i in range(5)]
    row = 0
    col = 0
    for element in key:
        if element in atoz:
            key_matrix[row] += element
            atoz = atoz.replace(element,'.')
            col+=1
            if(col>4):
                row+=1
                col = 0
    for element in atoz:
        if element!='.':
            key_matrix[row]+=element
            col+=1
            if col>4:
                row+=1
                col = 0
                
    #Rule 2
    '''
    If the letters appear on the same row of your table, replace them with the letters to 
    their immediate left respectively (wrapping around to the right side of the 
    row if a letter in the original pair was on the left side of the row).
    '''
    #Rule 3
    '''
    If the letters appear on the same column of your table, replace them with the 
    letters immediately above respectively (wrapping around to the bottom side of the 
    column if a letter in the original pair was on the top side of the column).
    '''
    #Rule 4
    '''
    If the letters are not on the same row or column, replace them with the 
    letters on the same row respectively but at the other pair of corners of the rectangle defined 
    by the original pair. The order is important – the first letter of the encrypted pair is 
    the one that lies on the same row as the first letter of the plaintext pair.
    '''
    result_str = ''
    for i in range(0,len(ciphertext),2):
        #Apply rule 2,3 or 4 for converting the ciphertext to plaintext
        pos0 = -1
        pos1 = -1
        pos2 = -1
        pos3 = -1
        for row in key_matrix:
            if((ciphertext[i] in row) and (ciphertext[i+1] in row)):
                pos0 = row.find(ciphertext[i])
                pos1 = row.find(ciphertext[i+1])
                result_str += row[(pos0-1)%5]
                result_str += row[(pos1-1)%5]
        if pos0!=-1 and pos1!=-1:
            continue
        element0 = ''
        element1 = ''
        for row in key_matrix:
            if(ciphertext[i] in row): 
                pos2 = row.find(ciphertext[i])
            if(ciphertext[i+1] in row):
                pos3 = row.find(ciphertext[i+1])
        if pos2!=pos3:
            for row in key_matrix:
                if(ciphertext[i] in row):
                    element0 = row[pos3]
                if(ciphertext[i+1] in row):
                    element1 = row[pos2]
            result_str += f'{element0}{element1}'
        
        else:
            for index, row in enumerate(key_matrix):
                if(ciphertext[i] in row):
                    element0 = key_matrix[(index-1)%5][pos2]
                if(ciphertext[i+1] in row):
                    element1 = key_matrix[(index-1)%5][pos3]
            result_str += f'{element0}{element1}'
    return result_str



            
        
        
            
          
        
    
    
    
        
                
         
    
