# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 22:46:06 2021

@author: nobin
"""
import caesar_cipher,monoalphabetic_cipher,otp,playfair_cipher,columnar,hill_cipher,numpy,onetimepad,keyed_columnar_transposition_cipher,polyalphabetic_cipher,railfence,shift_cipher
from flask import Flask,render_template,request,redirect,flash
page=Flask(__name__)
page.config['SECRET_KEY'] = 'super secret key'
userDetails={}
plaincipher=["Encrypted Ciphertext","Decrypted Plaintext "] 
ed=""
output=""
caesar_img="Caesar_Cipher.jpeg"
columnar_img="columnar.png"
hill_img="hill.png"
mono_img="monoalphabetic.img"
otp_img="otp.png"
playfair_img="playfair.png"
poly_img="polyalphabetic.png"
railfence_img="railfence.png"
shift_img="Shift_Cipher.png"
substitution_img="substitution.png"
image=""
hill_output=[]
intermediate=[]
@page.route("/",methods =["GET", "POST"])
def select():
    global userDetails,output,ed,plaincipher,image,hill_output,intermediate
    if request.method == 'POST':
        userDetails = request.form
        if userDetails['Encrypt']=="Encrypt":
            if userDetails["Algorithm"]=="Ceasar":
                output=caesar_cipher.caesar_encipher(userDetails['text'])
                ed=plaincipher[0]
                image=caesar_img
                return redirect("/output")
            elif userDetails["Algorithm"]=="Columnar":
                output=columnar.columnnar_encipher(int(userDetails["columnar-key"]), userDetails["text"])
                ed=plaincipher[0]
                image=columnar_img
                return redirect("/output")
            elif userDetails["Algorithm"]=="Hill":
                matrix_data=userDetails["hill_key"].split(",")
                if len(matrix_data)!=(int(userDetails["hill_size"])*int(userDetails["hill_size"])):
                    return "<h3>Incorrect Data</h3>"
                else:
                    temp=[]
                    while len(matrix_data)!=0:
                        temp.append(int(matrix_data[0]))
                        matrix_data.pop(0)
                        if len(temp)==int(userDetails["hill_size"]):
                            hill_output.append(temp)
                            temp=[]
                    output=hill_cipher.hill_encipher(userDetails["text"],numpy.matrix(hill_output))
                    ed=plaincipher[0]
                    image=hill_img
                    return redirect("/output")
            elif userDetails["Algorithm"]=="keyed-Columnar":
                strkey=userDetails["key_column_key"].split(",")
                actualkey=[]
                for key in strkey:
                    actualkey.append(int(key))
                output=keyed_columnar_transposition_cipher.keyed_column_trasposition_decipher(userDetails["text"],actualkey)
                ed=plaincipher[0]
                image=columnar_img
                return redirect("/output")
            elif userDetails["Algorithm"]=="Monoalphabetic":
                output=monoalphabetic_cipher.monoalphabetic_encipher(userDetails['text'])
                ed=plaincipher[0]
                image=mono_img
                return redirect("/output")
            elif userDetails["Algorithm"]=="otp":
                intermediate=otp.OTPencipher(userDetails['text'])
                output=intermediate[1]
                ed=plaincipher[0]
                image=otp_img
                return redirect("/output")
            elif userDetails["Algorithm"]=="playfair":
                output=playfair_cipher.playfair_encipher(userDetails['text'],userDetails['playfair-key'])
                ed=plaincipher[0]
                image=playfair_img
                return redirect("/output")
            elif userDetails["Algorithm"]=="Polyalphabetic":
                key=polyalphabetic_cipher.Key_length(userDetails['text'],userDetails['polyalphabetic-key'])
                output=polyalphabetic_cipher.polyalphabetic_encipher(userDetails['text'],key)
                ed=plaincipher[0]
                image=poly_img
                return redirect("/output")
            elif userDetails["Algorithm"]=="Railfence":
                output=railfence.railfence_encipher(userDetails['text'],int(userDetails['railfence_depth']))
                ed=plaincipher[0]
                image=railfence_img
                return redirect("/output")
            elif userDetails["Algorithm"]=="Shift":
                output=shift_cipher.encipher(userDetails['text'],int(userDetails['shift_key']))
                ed=plaincipher[0]
                image=shift_img
                return redirect("/output")
        elif userDetails['Encrypt']=="Decrypt":
            if userDetails["Algorithm"]=="Ceasar":
                output=caesar_cipher.caesar_decipher(userDetails['text'])
                ed=plaincipher[1]
                image=caesar_img
                return redirect("/output")
            elif userDetails["Algorithm"]=="Columnar":
                output=columnar.columnnar_decipher(int(userDetails["columnar-key"]), userDetails["text"])
                ed=plaincipher[1]
                image=columnar_img
                return redirect("/output")
            elif userDetails["Algorithm"]=="Hill":
                # return userDetails
                matrix_data=userDetails["hill_key"].split(",")
                if len(matrix_data)!=(int(userDetails["hill_size"])*int(userDetails["hill_size"])):
                    return "<h3>Incorrect Data</h3>"
                else:
                    temp=[]
                    while len(matrix_data)!=0:
                        temp.append(int(matrix_data[0]))
                        matrix_data.pop(0)
                        if len(temp)==int(userDetails["hill_size"]):
                            hill_output.append(temp)
                            temp=[]
                    output=hill_cipher.hill_decipher(userDetails["text"],numpy.matrix(hill_output))
                    ed=plaincipher[1]
                    image=hill_img
                    return redirect("/output")
            elif userDetails["Algorithm"]=="keyed-Columnar":
                output=keyed_columnar_transposition_cipher.keyed_column_trasposition_decipher(userDetails["text"],userDetails["key_column_key"])
                ed=plaincipher[1]
                image=columnar_img
                return redirect("/output")
            elif userDetails["Algorithm"]=="Monoalphabetic":
                output=monoalphabetic_cipher.monoalphabetic_decipher(userDetails['text'])
                ed=plaincipher[1]
                image=mono_img
                return redirect("/output")
            elif userDetails["Algorithm"]=="otp":
                output=otp.OTPencipher(userDetails['text'])
                ed=plaincipher[1]
                image=otp_img
                return redirect("/output")
            elif userDetails["Algorithm"]=="otp":   
                output = onetimepad.decrypt(userDetails['text'], 'random')        
                ed=plaincipher[1]
                image=otp_img
                return redirect("/output")
            elif userDetails["Algorithm"]=="playfair":
                output=playfair_cipher.playfair_decipher(userDetails['text'],userDetails['playfair-key'])
                ed=plaincipher[1]
                image=playfair_img
                return redirect("/output")
            elif userDetails["Algorithm"]=="Polyalphabetic":
                key=polyalphabetic_cipher.Key_length(userDetails['text'],userDetails['polyalphabetic-key'])
                output=polyalphabetic_cipher.polyalphabetic_decipher(userDetails['text'],key)
                ed=plaincipher[1]
                image=poly_img
                return redirect("/output")
            elif userDetails["Algorithm"]=="Railfence":
                output=railfence.railfence_decipher(userDetails['text'],int(userDetails['railfence_depth']))
                ed=plaincipher[1]
                image=railfence_img
                return redirect("/output")
            elif userDetails["Algorithm"]=="Shift":
                output=shift_cipher.decipher(userDetails['text'],int(userDetails['shift_key']))
                ed=plaincipher[1]
                image=shift_img
                return redirect("/output")
    return render_template("home.html")
@page.route("/output")
def caesar():
    global output,ed,typ
    return render_template("caesar.html",output=output,ed=ed,image=image)

if __name__ == '__main__':
    page.run(host='0.0.0.0', debug=True,port=5000)