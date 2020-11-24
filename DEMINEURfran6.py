import random # nous permetras d'utiliser de l'aleatoire
import time # permettra d'afficher le temps

def initDemineur():     # permet d'afficher le titre du jeu pour marquer le debut de partie
    print('#########')
    print('DEMINEUR')
    print('#########')

def displayTab(tableau):
    print('\n')          # permet de faire un saut a la ligne
    for i in tableau:
        print(i)

def initTabAff(): # demande au joueur la taille du jeu avnt de la creer
    tabAff=[]
    print('Déterminer la taille de votre démineur (difficulté)')
    ligne=int(input("Entrer le nombre de ligne: "))
    colonne=int(input("Entrer le nombre de colonne: "))
    for i in range(ligne+2):
        tabAff.append([])
        for j in range(colonne+2):
            tabAff[i].append('?')
    
  
    for i in range(colonne+2): # Rajoute deux lignes de contour sur l'interface
            tabAff[0][i]="#"
            tabAff[ligne+1][i]="#"
    
    for i in range(ligne+2): # Rajoute deux colonnes de contour sur l'interface
        tabAff[i][0]="#"
        tabAff[i][colonne+1]="#"
    return tabAff

def initTabJeu(tableau): # creation du tableau comportant les mines
    tabJeu=tableau
    for i in range(1,len(tableau)-1):
        for j in range(1,len(tableau[0])-1):
            tabJeu[i][j]=random.randint(0,1) # Place aléatoirement des 0 et des 1 dans le tableau de jeu
            if tabJeu[i][j]==1: # Si c'est un 1 remplace par une * (mine) (les nombres nous seront nécessaire pour afficher le nb de mines adjacentes)
                tabJeu[i][j]='*'
                if tabJeu[i-1][j]=='*' or tabJeu[i][j-1]=='*': # Supprime la mine si il ya déjà une mine adjacente (en haut et à gauche)
                    tabJeu[i][j]=0
    return tabJeu

def initProximite(tableau): # creation du tableau avec la proximité des mines
    for i in range(1,len(tableau)-1):
        for j in range(1,len(tableau[0])-1):
            varProx=0
            if tableau[i][j]==0:
                if tableau[i-1][j]=='*': # Si mine à proxi au dessus
                    varProx=varProx+1
                if tableau[i][j-1]=='*': # Si mine à proxi à gauche
                    varProx=varProx+1
                if tableau[i-1][j-1]=='*': # Si mine à proxi coin sup gauche
                    varProx=varProx+1
                if tableau[i][j+1]=='*': # Si mine à proxi à droite
                    varProx=varProx+1
                if tableau[i+1][j]=='*': # Si mine à proxi en dessous
                    varProx=varProx+1
                if tableau[i+1][j+1]=='*': # Si mine à proxi coin inf droite
                    varProx=varProx+1
                if tableau[i-1][j+1]=='*': # Si mine à proxi coin sup droite
                    varProx=varProx+1
                if tableau[i+1][j-1]=='*': # Si mine à proxi coin inf gauche
                    varProx=varProx+1
                tableau[i][j]=varProx
    return tableau

# Lancement des fonctions de jeu
initDemineur() 

tabAff=initTabAff()
displayTab(tabAff)



tabJeu=initTabJeu(tabAff)
displayTab(tabJeu)

displayTab(initProximite(tabJeu))

Jouer(initProximite)


# Boucle de jeu


def Jouer(): 
    print("Choisir une case")
    varLigne=int(input("Choisir le numéro de la ligne: "))
    varColonne=int(input("Choisir le numéro de la colonne: "))
    print(tabAff[varLigne[varColonne]])
    

    return tabAff



t1=time.time() #En début de partie
t2=time.time() #En fin de partie avec print(t2-t1)
tFin=t2-t1 