import sys
import subprocess
import os
from time import sleep
from config import *

w1 = "EDITEZ LA CONFIG AVANT D'UTILISER\n"

def worker(file,token):
    print(token + " " + fichier)
    subprocess.call(file, shell=True)

for char in w1:
    sleep(0.01)
    sys.stdout.write(char)
    sys.stdout.flush()
sleep(0.5)
print("Tapez un des nombres suivants des mots à spammmer")
print("1 : Image Spammer - Spam des images aléatoirements")
print("2 : Insultes Spammer - Prends des insultes et les spams")
print("3 : Texte Spammer - écris le texte à spammer")

in_pick = float(input("Choisissez un bot: "))

if in_pick == 1:
    for token in TokenDeLutilisateur:
        p = subprocess.Popen(['python', 'image_spam.py', token],shell=True)
            
if in_pick == 2:
    for token in TokenDeLutilisateur:
        p = subprocess.Popen(['python','insultes_spam.py', token],shell=True)
        
if in_pick == 3:
    spam_texte = input("écrivez le texte à spam : ")
    print('python texte_spam.py ' + "'"+spam_texte+"'")
    for token in TokenDeLutilisateur:
        print('Chargement Token')
        p = subprocess.Popen(['python','texte_spam.py',token,spam_texte],shell=True)
        sleep(1)
        print("Token chargé.")
        print(' ')
p.wait()
