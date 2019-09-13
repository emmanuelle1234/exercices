# -*- coding: utf-8 -*-
"""
ZCasino
Created on Thu Sep 12 16:54:42 2019
@author: Emmanuelle
"""


from random import randrange
from math import ceil

play_again=True 


def play_again_process(x):
    """Propose de rejouer ou pas en fonction d'une réponse x et renvoie play_again"""
    while x!="oui" and x!="Oui" and x!="Oui." and x!="Oui!" and x!="Oui !" and x!="oui." and x!="oui !" and x!="non" and x!="Non" and x!="Non." and x!="Non!" and x!="Non !" and x!="non." and x!="non !":
        print("Je vous prie de bien vouloir m'excuser, je n'ai pas compris.")
        print("Si vous souhaitez rejouer, merci de taper : oui.")
        print("Si vous ne souhaitez pas rejouer, merci de taper : non.")
        x=input("Alors, souhaitez-vous rejouer ? ")
    if x=="oui" or x=="Oui" or x=="Oui." or x=="Oui!" or x=="Oui !" or x=="oui." or x=="oui !":
        play_again=True
    else:   
        play_again=False        
    return play_again
    

print()
print("Bienvenue au Casino de la Chance !")
money=input("De combien d'argent (en euros) disposez-vous pour tenter votre chance ? ")
money=float(money)

while play_again==True:
    
    nb_player=50
    while nb_player>49 or nb_player<0:
        nb_player=input("Veuillez indiquer le nombre entre 0 et 49 sur lequel vous misez : ")
        try:
            nb_player=int(nb_player)
        except ValueError:
            nb_player=input("Merci d'indiquer un NOMBRE entre 0 et 49 : ")
        if nb_player>49:
            nb_player=input("Merci d'indiquer un nombre inférieur 49 : ")
        else:
            nb_player=input("Merci d'indiquer un nombre supérieur ou égal à 0 : ")
    
    nb_player=int(nb_player)   
    sum=input("Quelle somme (en euros) misez-vous sur ce nombre ? ")
    sum=float(sum)
   
    i=0
    while i<3 and money-sum<0:
        print("Désolé mais vous ne pouvez pas miser plus que ce que vous avez.")
        sum=input("Quelle somme voulez-vous miser ? Elle doit être inférieure à ce que vous avez : ")
        sum=float(sum)
        i+=1
    if i==3:
        print("Désolé, il vaut mieux rentrer chez vous.")
        print("Pourquoi pas à une prochaine fois quand vous serez plus réveillé ?")
        break
    money=money-sum
    print()
    nb=randrange(50)
    print("Le numéro gagnant est...", nb, " !")
    
    if nb_player==nb:
        output=ceil(sum*3)
        money=money+output
        print("Félicitations ! Vous avez misé sur le nombre gagnant !")
        print("Vous disposez maintenant de", money, "euros.")
        play_answer=input("Avec cette chance aujourd'hui, voulez-vous miser à nouveau ?")
    elif (nb_player%2 == 0 and nb%2 == 0) or (nb_player%2 != 0 and nb%2 != 0):
        output=ceil(sum*0.5)
        money=money+output
        print("Pas mal ! Vous avez misé sur la bonne couleur.")
        print("Vous disposez maintenant de", money, "euros.")
        play_answer=input("Voulez-vous tenter à nouveau le bon nombre ? ")   
    else: 
        output=0
        print("Dommage : vous avez perdu.")
        print("Vous disposez maintenant de", money, "euros.")
        play_answer=input("Mais rien n'est jamais définitivement perdu : et si vous retentiez votre chance ? ")
    
    play_answer=str(play_answer)    
    play_again=play_again_process(play_answer)
    
    if play_again==False:
        print()
        print("A une prochaine fois !")
        
    if money==0:
        print("J'ai bien peur que vous n'ayiez plus un sou. A une prochaine fois !")
        break
   
   #cas où il reste 0 à revoir 
   #les différents cas où des lettres sont saisies à la place de chiffres (chapitre exceptions)
    






    

