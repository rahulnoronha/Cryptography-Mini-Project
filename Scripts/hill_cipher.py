# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2

@author: Rahul Noronha
"""

import numpy as np
from egcd import egcd
import string

atoz = string.ascii_lowercase
letter_to_index = dict(zip(atoz, range(len(atoz))))
index_to_letter = dict(zip(range(len(atoz)), atoz))

def matrix_inv_mod(matrix, number):
    '''
    Function to the find the Matrix inverse modulus number
    '''
    det = int(np.round(np.linalg.det(matrix))) 
    det_inv = egcd(det, number)[1] % number  # Step 2)
    try:
        matrix_modulus_inv = (
        det_inv * np.round(det * np.linalg.inv(matrix)).astype(int) % number
        )
    except Exception as e:
        return 'Singular Matrix'
    return matrix_modulus_inv

def hill_encipher(plaintext, K):
    plaintext = plaintext.lower()
    result_text = ""
    plaintext_in_numbers = []
    for letter in plaintext:
        plaintext_in_numbers.append(letter_to_index[letter])
    split_plaintext = [
        plaintext_in_numbers[i : i + int(K.shape[0])]
        for i in range(0, len(plaintext_in_numbers), int(K.shape[0]))
    ]
    for P in split_plaintext:
        P = np.transpose(np.asarray(P))[:, np.newaxis]
        while P.shape[0] != K.shape[0]:
            P = np.append(P, letter_to_index['x'])[:, np.newaxis]
        numbers = np.dot(K, P) % len(atoz)
        n = numbers.shape[0]
        for index in range(n):
            number = int(numbers[index, 0])
            result_text += index_to_letter[number]
    return result_text

def hill_decipher(ciphertext, K):
    ciphertext = ciphertext.lower()
    Kinv = matrix_inv_mod(K, len(atoz))
    if(str(Kinv)!='Singular Matrix'):
        result_text = ""
        ciphertext_in_numbers = []

        for letter in ciphertext:
            ciphertext_in_numbers.append(letter_to_index[letter])

        split_ciphertext = [
            ciphertext_in_numbers[i : i + int(Kinv.shape[0])]
            for i in range(0, len(ciphertext_in_numbers), int(Kinv.shape[0]))
        ]

        for C in split_ciphertext:
            C = np.transpose(np.asarray(C))[:, np.newaxis]
            numbers = np.dot(Kinv, C) % len(atoz)
            n = numbers.shape[0]

            for index in range(n):
                number = int(numbers[index, 0])
                result_text += index_to_letter[number]

        return result_text
    else:
        return 'Matrix is not invertible in modulo 26'