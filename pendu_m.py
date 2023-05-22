#Laetitia GRANAL
#jeu du pendu

import random

# Choisi un mot aléatoire à partir du fichier mots_pendu.txt donné dans le moodle
def liste_mots():
    mots = []
    with open('mots_pendu.txt', 'r') as f:
        mots = f.readlines() #récupère les mots en lisant les lignes une par une
    return random.choice(mots).strip() #récupère un mots aléatoire en supprimant tout interlignage

# Affiche le mot actuel non trouvé
def afficher_mot(mot, lettres_actuelles):
    mot_actuel = ""

    for i in mot:

        #affiche les lettres du mot actuel
        if i in lettres_actuelles:
            mot_actuel += i

        #affiche les lettres restantes
        else:
            mot_actuel += "_"
    print( mot_actuel)

def renvoie_mot(mot, lettres_actuelles):
    global mot_act
    mot_actuel = ""

    for i in mot:

        #affiche les lettres du mot actuel
        if i in lettres_actuelles:
            mot_actuel += i

        #affiche les lettres restantes
        else:
            mot_actuel += "_"
    return mot_actuel


# Début du jeu
def jouer_pendu():
    mot = liste_mots()
    lettres_trouvees = [] #listes les lettres trouvées correctes
    lettres_rentree = [] # lites les lettres déjà rentrée
    nb_chances = 6

    print("Bienvenue dans le jeu du pendu !")

    #Condition tant que le mot n'a pas été trouvé
    while mot != renvoie_mot(mot, lettres_trouvees) :
        print("\nDevinez le mot :")

        #affiche le mot dans son état actuel
        afficher_mot(mot, lettres_trouvees)

        #condition de défaite qui casse la boucle while
        if nb_chances == 0:
            print(f"Perdu ! Plus de chances disponibles! Le mot était {mot}.")
            break

        print(f"\nChances disponibles : {nb_chances}")

        #variable récupérant la lettres entrée
        i = input("Veuillez entrer une lettre : ").lower()

        #vérifie si la lettre a déjà été rentrée
        if i in lettres_rentree:
            print("Vous avez déjà trouvé cette lettre.")
            continue

        #lettres données par le joueur est ajouté à la liste
        lettres_rentree.append(i)

        #vérifie si la lettre appartient au mot
        if i in mot:
            #La bonne lettre est ajouté à la liste des lettres déjà trouvés
            print(f"Bonne lettre ! La lettre {i} appartient au mot.")
            lettres_trouvees.append(i)
        else:
            #ne nombre de cha,ce diminue si c'est une mauvaise lettre
            print(f"Mauvaise lettre ! La lettre {i} n'appartient pas au mot.")
            nb_chances -= 1

        #affiche au joueur les lettres déjà rentrées
        print("Lettres déjà utilisées :", lettres_rentree)

    #condition pour indiquer que le jouer a gagné
    if mot == renvoie_mot(mot, lettres_trouvees) :
        print(f"Félicitations ! Vous avez deviné le mot {mot}.")

# Démarre le jeu
jouer_pendu()
