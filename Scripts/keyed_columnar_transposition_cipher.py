# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2

@author: Rahul Noronha
"""
import string

#Keyed Columnar Transposition cipher combines the keyed transposition cipher 
#and then uses transposition techniques to read ciphertext column to column

def keyed_column_trasposition_encipher(plaintext, key):
    atoz = string.ascii_lowercase
    plaintext = plaintext.lower()
    new=''
    for i in plaintext:
        if(i not in atoz):
            pass
        else:
            new+=i
    plaintext = new
    key_map = dict(zip(range(0,len(key)),key))
    print(key_map)
    while(len(plaintext)%len(key)!=0):
        plaintext+='x'
    row_wise = ['' for i in range(int(round(len(plaintext)/len(key))))]
    for i in range(0,int(round(len(plaintext)/len(key)))):
        for j in range(len(key)):
            row_wise[i]+=plaintext[len(key)*i+j]

    transposed = ['' for i in range(int(round(len(plaintext)/len(key))))]
    for ind,element in enumerate(row_wise):
        for index in range(len(element)):
            transposed[ind]+=element[key_map[index]-1]
    print(transposed)    
    result_text = ''
    for i in range(len(key)):
        for element in transposed:
            result_text+= element[i]
    return result_text
    
def keyed_column_trasposition_decipher(ciphertext, key):
    ciphertext = ciphertext.lower()
    key_map = dict(zip(key,range(0,len(key))))
    print(key_map)
    col_wise = ['' for i in range(int(round(len(ciphertext)/len(key))))]
    for i in range(len(key)):
        for j in range(int(round(len(ciphertext)/len(key)))):
            col_wise[j]+= ciphertext[i*int(round(len(ciphertext)/len(key)))+j]
    transposed = ['' for i in range(int(round(len(ciphertext)/len(key))))]
    for ind,element in enumerate(col_wise):
        for index in range(len(element)):
            transposed[ind]+=element[key_map[index+1]]
    print(transposed)    
    result_text = ''

    for element in transposed:
        for i in range(len(key)):
            result_text+= element[i]
    return result_text
    
    
print(keyed_column_trasposition_encipher('attack tonight',[1,2,3,4,5]))
        
        
    
    
