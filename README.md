# pendu
jeu pendu en python
Le principe du jeu est de trouver un mot en entrant différentes lettres. Ces mots sont contenant dans un document textes et pris aléatoirement.
Il n'y a que 6 chances. Des lettres ne peuvent pas êtres utilisées plusieurs fois. Une liste contenant les lettres utilisées sont affiché pour l'utilisateur.
Après les 6 chances, le mot est dévoilé et le joueur à perdu. Vous pouvez entrer les lettres majuscules ou minuscules.

Ce code est composé de 4 fonctions
liste_mots(): renvoie un mot aléatoire de la liste donnée sur moodle
afficher_mot(mot, lettres_actuelles) : cette fonction affiche le mot du pendu en l'état
renvoie_mot(mot, lettres_actuelles) : renvoie le mot
jouer_pendu(): lance le jeu du pendu 
