# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2

@author: Rahul Noronha
"""
import string

#Columnar Transposition cipher is the keyed transposition cipher 

def columnar_transposition_encipher(plaintext, key):
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
    while(len(plaintext)%len(key)!=0):
        plaintext+='x'
    row_wise = ['' for i in range(int(round(len(plaintext)/len(key))))]
    for i in range(len(key)):
        for j in range(0,int(round(len(plaintext)/len(key)))):
            row_wise[j]+=plaintext[len(key)*j+i]

    transposed = ['' for i in range(int(round(len(plaintext)/len(key))))]
    for ind,element in enumerate(row_wise):
        for index in range(len(element)):
            transposed[ind]+=element[key_map[index]-1]  
    result_text = ''
    for element in transposed:
        for i in range(len(key)):
            result_text+= element[i]
    return result_text
    
def columnar_transposition_decipher(ciphertext, key):
    ciphertext = ciphertext.lower()
    key_map = dict(zip(key,range(0,len(key))))
    row_wise = ['' for i in range(int(round(len(ciphertext)/len(key))))]
    for i in range(int(round(len(ciphertext)/len(key)))):
        for j in range(len(key)):
            row_wise[i]+= ciphertext[i*len(key)+j]
    print(row_wise)
    transposed = ['' for i in range(int(round(len(ciphertext)/len(key))))]
    for ind,element in enumerate(row_wise):
        for index in range(len(element)):
            transposed[ind]+=element[key_map[index+1]]   
    result_text = ''
    print(transposed)
    for element in transposed:
        for i in range(len(key)):
            result_text+= element[i]
    return result_text

print(columnar_transposition_decipher('ruhlanornohubta',[1,4,3,5,2]))