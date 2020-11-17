#Imports
from random import randrange
from math import ceil

#Variables
argent = 1000

#Fonctions
def choix():
    mise = int(input("Combien voulez vous miser ? \n"))
    if mise > argent:
        print("Vous n'avez pas assez d'argent !!")
        mise = -1
    if mise < 0:
        print("Vous allez bien monsieur ?\nJe pense que vous avez assez bu.")
        mise = -1
    user = int(input("Sur quelle case voulez vous miser.\n"))
    if user < 1:
        print("Vous allez bien monsieur ?\nJe pense que vous avez assez bu.")
        user = -1
    if user > 50:
        print("Vous allez bien monsieur ?\nJe pense que vous avez assez bu.")
        user = -1
    if not (user == -1 or mise == -1):
        print("Vous misez donc " + str(mise) + " € sur la case " + str(user) + ".")
    return mise,user

def roulette():
    comp = randrange(1,50)
    print("La roulette tourne et la boule tombe sur " + str(comp) + " !!!")
    return comp

def gains(user,comp,mise):
    if (user == comp):
        gains = mise*3
        print("Bien joué vous avez joué la case "+ str(user) +" et vous etes tombé dessus.")
    elif (user == comp%2):
        gains = ceil(mise*0.5)
        print("La bille est tombée sur la case de la meme couleur.")
    else:
        gains = 0
        print("Dommage, vous ne gagnez rien.")
    return gains

#Programme

while argent > 0:
    print("Vous avez " + str(argent) + " €.")
    mise,user = choix()
    if not(user == -1 or mise == -1):
        comp = roulette()
        argent -= mise
        argent += gains(user, comp, mise)