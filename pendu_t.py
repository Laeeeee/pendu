import random

# Choisi un mot aléatoire à partir du fichier mots_pendu.txt donné dans le moodle
def liste_mots():
    mots = []
    with open('mots_pendu.txt', 'r') as f:
        mots = f.readlines() #récupère les mots en lisant les lignes une par une
    return random.choice(mots).strip() #récupère un mots aléatoire

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
    print(mot_actuel)

# Début du jeu
def jouer_pendu():
    mot = liste_mots()
    lettres_trouvees = [] #listes les lettres trouvées correctes
    lettres_rentree = [] # lites les lettres déjà rentrée
    nb_chances = 6

    print("Bienvenue dans le jeu du pendu !")

    while True:
        print("\nDvinez le mot :")
        afficher_mot(mot, lettres_trouvees)

        if set(mot) == set(lettres_trouvees):
            print("Félicitations ! Vous avez deviné le mot '{}'.".format(mot))
            break

        if nb_chances == 0:
            print("Perdu ! Plus de chances disponibles! Le mot était '{}'.".format(mot))
            break

        print("\nChances disponibles : {}".format(nb_chances))

        #variable récupérant la lettres entrée
        i = input("Veuillez entrer une lettre ou le mot complet : ").lower()

        if i in lettres_rentree:
            print("Vous avez déjà trouvé cette lettre.")
            continue

        if i in lettres_trouvees:
            print("Vous avez déjà trouvé cette lettre.")
            continue

        #lettres données par le joueur
        lettres_rentree.append(i)

        if i in mot:
            print("Bonne lettre ! La lettre '{}' appartient au mot.".format(i))
            lettres_trouvees.append(i)
        else:
            print("Mauvaise lettre ! La lettre '{}' n'appartient pas au mot.".format(i))
            nb_chances -= 1

        print("Lettres déjà utilisées :", lettres_rentree)

# Démarre le jeu
jouer_pendu()
