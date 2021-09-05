#A caesar cipher is a cipher in which each letter in the message is substituted by a letter 3 letters down the alphabet.
#The shift k is an integer value in between 0 and 25. The Caesar cipher is a specialized case of the Caesar cipher.
#In the Caesar cipher, the k value is fixed to 3.
#Let us import the functions from shift_cipher.py and make key as 3 in order to create a Caesar Cipher.

#Importing the python file shift_cipher.py and its functions
import shift_cipher

def caesar_encipher(plaintext):
    '''
    This function takes in a plaintext p, and key k and enciphers the text using the formula given below
    c = (p+3) mod(26)
    
    '''
    return shift_cipher.encipher(plaintext,3)

def caesar_decipher(ciphertext):
    '''
    This function takes in a ciphertext c, and key k and deciphers the text using the formula given below
    p = (c-3) mod(26)
    
    '''
    return shift_cipher.decipher(ciphertext,3)