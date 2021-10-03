# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 16:47:14 2021

@author: nobin
"""
import random
key=[]

def otp_encipher(string):
    global key
    string_list=[]
    cipher=[]
    for letter in string:
        key.append(random.choice(['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']))
        string_list.append(letter) 
    for i in range(0,len(string_list)):
        cipher.append(ord(string_list[i]) ^ ord(key[i]))
    cipher_text=""
    for letter in cipher:
        cipher_text=cipher_text+chr(letter)
    print("Cipher text is",cipher_text)
    return cipher_text
def otp_decipher(string):
    global key
    plaintext=[]
    text=[]
    for i in range(0,len(string)):
        text.append(chr(string[i]))
    for i in range(0,len(key)):
        plaintext.append(ord(text[i]) ^ ord(key[i]))
    for i in range(0,len(plaintext)):
        plaintext[i]=chr(plaintext[i])
    proper_text=""
    for number in plaintext:
        proper_text=proper_text+number
    return proper_text

