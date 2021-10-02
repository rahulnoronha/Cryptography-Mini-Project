#A shift cipher is a cipher in which each letter in the message is substituted by a letter a few letters down the alphabet.
#The shift k is an integer value in between 0 and 25.

def encipher(plaintext, key):
    '''
    This function takes in a plaintext p, and key k and enciphers the text using the formula given below
    c = (p+k) mod(26)
    
    '''
    plaintext = plaintext.lower()
    result = ""
    #Loop used to traverse the characters of the plaintext
    for i in range(len(plaintext)):
        char = plaintext[i]
        
        #If a number or special character is encountered, keep it as it is
        
        if(char.isalpha()!=1):
            result += char
        # Encrypt uppercase characters
        elif (char.isupper()):
            result += chr((ord(char) + key-65) % 26 + 65)
 
        # Encrypt lowercase characters
        else:
            result += chr((ord(char) + key - 97) % 26 + 97)
 
    return result

def decipher(ciphertext, key):
    '''
    This function takes in a ciphertext c, and key k and deciphers the text using the formula given below
    p = (c-k) mod(26)
    
    '''
    result = ""
    #Loop used to traverse the characters of the ciphertext
    for i in range(len(ciphertext)):
        char = ciphertext[i]
        
        #If a number or special character is encountered, keep it as it is
        
        if(char.isalpha()!=1):
            result += char
        # Encrypt uppercase characters
        elif (char.isupper()):
            result += chr((ord(char) - key-65) % 26 + 65)
 
        # Encrypt lowercase characters
        else:
            result += chr((ord(char) - key - 97) % 26 + 97)
 
    return result

    