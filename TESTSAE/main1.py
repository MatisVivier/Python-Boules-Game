#####   import  #####

from upemtk import *
from math import *
from time import *
from random import randint



#####   Fonctions   #####



def temps_tours(milliseconds):
    t1 = time() + milliseconds / 1000      #On prend la fonction attendre_touche_jusqua dans upemtk, on fait quelques ajustements pour attendre un clic
    while time()<t1:
        ev = donne_evenement()
        type_ev = type_evenement(ev)
        if type_ev == "ClicDroit" or type_ev == "ClicGauche":
            return clic_x(ev), clic_y(ev), type_ev
        mise_a_jour()
    return None


def touche_bord_bleu(x1, y1, r) :  

    '''
    x1 + r c'est pour savoir si sa dépasse à droite
    x1 - r c'est pour savoir si sa dépasse à gauche
    y1 + r c'est pour savoir si sa dépasse en bas
    y1 - r c'est pour savoir si sa dépasse en haut

    '''

    if (x1+r > 590 or x1-r < 10):
        return False
    if (y1+r > 570 or y1-r < 50):
        return False   


def touche_bord_rouge(x2, y2, r) :  

    if x2+r > 590 or x2-r < 10:
        return False
    if y2+r > 570 or y2-r < 50:
        return False


def intersection_bleu(liste, x1, y1, r):
    inter = False
    for i in range(len(liste)):
        distance = sqrt((x1 - liste[i][0])**2 + (y1 - liste[i][1])**2) #calcule la distance entre les deux points
        if r < distance < r*2:
            inter = True
    return inter



def intersection_rouge(liste, x2, y2, r):
    inter = False
    for i in range(len(liste)):
        distance = sqrt((x2 - liste[i][0])**2 + (y2 - liste[i][1])**2) #calcule la distance entre les deux points
        if r < distance < r*2:
            inter = True
    return inter

def intersection_obstacle(liste, x, y, r):
    inter = False
    for i in range(len(liste)):
        distance = sqrt((x - liste[i][0])**2 + (y - liste[i][1])**2) #calcule la distance entre les deux points
        if distance < r*2:
            inter = True
    return inter



def clic_interieur(liste, x, y):    #On verifie qu'on a cliqué a l'interieur d'un cercle ennemi
    inter = False
    for i in range(len(liste)):
        distance = sqrt((x - liste[i][0])**2 + (y - liste[i][1])**2) #calcule la distance entre les deux points
        if distance < liste[i][3]:
            inter = True
    return inter

def clic_interieur_position(liste, x, y):    #On verifie qu'on a cliqué a l'interieur d'un cercle ennemi
    for i in range(len(liste)):
        distance = sqrt((x - liste[i][0])**2 + (y - liste[i][1])**2) #calcule la distance entre les deux points
        if distance < liste[i][3]:
            return i

def separation(liste, x, y, surface, i, couleur):
    rayon_cercle_clic = 0
    nouveau_x = 0
    nouveau_y = 0
    rayon_deuxieme_cercle = 0
    nouvelle_liste = []
    distance = sqrt((x - liste[i][0])**2 + (y - liste[i][1])**2) #calcule la distance entre les deux points
    rayon_cercle_clic = liste[i][3] - distance # calcul du rayon du cercle créer
    rayon_deuxieme_cercle = liste[i][3] - rayon_cercle_clic #calcul du rayon du deuxième cercle créer
    hypothenus = sqrt((rayon_cercle_clic)**2 + (rayon_cercle_clic+rayon_deuxieme_cercle)**2) #calcul de l'hypothénus
    if x>=liste[i][0] and y>=liste[i][1]: #calcul quand le clique se trouve dans le coins supperieur droit du cercle de base
        nouveau_x = x - (liste[i][3] * (rayon_cercle_clic+rayon_deuxieme_cercle)/hypothenus)
        nouveau_y = y - (liste[i][3] * rayon_cercle_clic/hypothenus)
        efface(liste[i][2])
        liste[i][2] = 0
    elif x>=liste[i][0] and y<=liste[i][1]: #calcul quand le clique se trouve dans le coins inferieur droit du cercle de base
        nouveau_x = x - (liste[i][3] * (rayon_cercle_clic+rayon_deuxieme_cercle)/hypothenus)
        nouveau_y = y + (liste[i][3] * rayon_cercle_clic/hypothenus)
        efface(liste[i][2])
        liste[i][2] = 0
    elif x<=liste[i][0] and y<=liste[i][1]: #calcul quand le clique se trouve dans le coins inferieur gauche du cercle de base
        nouveau_x = x + (liste[i][3] * (rayon_cercle_clic+rayon_deuxieme_cercle)/hypothenus)
        nouveau_y = y + (liste[i][3] * rayon_cercle_clic/hypothenus)
        efface(liste[i][2])
        liste[i][2] = 0
    elif x<=liste[i][0] and y>=liste[i][1]: #calcul quand le clique se trouve dans le coins supperieur gauche du cercle de base
        nouveau_x = x + (liste[i][3] * (rayon_cercle_clic+rayon_deuxieme_cercle)/hypothenus)
        nouveau_y = y - (liste[i][3] * rayon_cercle_clic/hypothenus)
        efface(liste[i][2])
        liste[i][2] = 0
    surface += (rayon_cercle_clic**2)*pi + (rayon_deuxieme_cercle**2)*pi #calcul de la surface entre les deux cercles créer
    nouvelle_liste.append([[x, y, rayon_cercle_clic], [nouveau_x, nouveau_y, rayon_deuxieme_cercle]])
    return nouvelle_liste 

def grandi(liste, r, x, y):     #On verifie la distance entre les cercles pour savoir si on agrandi le rayon ou non
    inter = False
    for i in range(len(liste)):
        distance = sqrt((x - liste[i][0])**2 + (y - liste[i][1])**2) #calcule la distance entre les deux points
        if distance < r*2:
            inter = True
    return inter


def rayon_grandi(liste, liste2):    #On a grandi le rayon
    for i in range(len(liste)):
        if grandi(liste2, liste[i][3], liste[i][0], liste[i][1]) == False:
            liste[i][3] += 5
    return liste

def ecran_fin_de_jeu(surfacebleu, surfacerouge):
    mise_a_jour()
    sleep(2) #marque une pause avant l'ecran des scores
    rectangle(80, 160, 520, 350, remplissage='beige')
    texte(100, 210, "Fin du match ! \ncliquer pour voir vos résultat !", police = "Montserrat", taille= 15) #On attend un clique pour tout effacer et laisser place aux scores
    attente_clic()
    efface_tout()
    ## Gagnant (rouge ou bleu), égalité ### On afficher donc les scores de chaque equipes pour pouvoir comparer
    #Nous calculons le score grace a la surface de chaque cercle
    rectangle(80, 160, 300, 350, remplissage='#1b71db')
    rectangle(300, 160, 520, 350,  remplissage='#c80c25')
    if surfacebleu > surfacerouge:  #Gagnant Bleu
        texte(100, 210, "L'equipe bleu Gagne ! \nvous avez obtenu \nun score de : ", police = "Montserrat", taille= 12, couleur="white")
        texte(155, 300, int(surfacebleu), police = "Montserrat", taille= 12, couleur="white")
        texte(325, 210, "Vous avez perdu ! \nvous avez obtenu \nun score de : ", police = "Montserrat", taille= 12, couleur="white")
        texte(375, 300, int(surfacerouge), police = "Montserrat", taille= 12, couleur="white")

    if surfacerouge > surfacebleu: #Gagnant Rouge
        texte(325, 210, "L'equipe rouge Gagne ! \nvous avez obtenu \nun score de : ", police = "Montserrat", taille= 12, couleur="white")
        texte(375, 300, int(surfacerouge), police = "Montserrat", taille= 12, couleur="white")
        texte(100, 210, "Vous avez perdu ! \nvous avez obtenu \nun score de : ", police = "Montserrat", taille= 12, couleur="white")
        texte(155, 300, int(surfacebleu), police = "Montserrat", taille= 12, couleur="white")
        
    if surfacebleu == surfacerouge: #Egalité
        texte(325, 210, "Egalite ! \nvous avez obtenu \nun score de : ", police = "Montserrat", taille= 12, couleur="white")
        texte(375, 300, int(surfacerouge), police = "Montserrat", taille= 12, couleur="white")
        texte(100, 210, "Egalite ! \nvous avez obtenu \nun score de : ", police = "Montserrat", taille= 12, couleur="white")
        texte(155, 300, int(surfacebleu), police = "Montserrat", taille= 12, couleur="white")

    attente_clic()
    efface_tout()
    liste_score = []
    liste_meilleur = []
    scorebleu = int(surfacebleu)
    scorerouge = int(surfacerouge)
    f = "classement.txt"
    with open(f, "a") as fichier:
        fichier.write(str(scorebleu))
        fichier.write("\n")
        fichier.write(str(scorerouge))
        fichier.write("\n")
    with open(f, "r") as fichier:
        ligne = fichier.readline()
        for ligne in fichier:
            liste_score.append(ligne.split())
    for i in range(len(liste_score)):
        for j in range(len(liste_score[0])):
            liste_meilleur.append(int(liste_score[i][j]))
    liste_meilleur.sort(reverse = True)
    rectangle(80, 175, 230, 400, remplissage='#adacac')
    rectangle(230, 130, 380, 400, remplissage='#d4ab0b')
    rectangle(380, 210, 530, 400, remplissage='#9e634c')

    texte(200, 15, "CLASSEMENT GLOBAL", police = "Montserrat", taille= 18, couleur="black")

    texte(240, 100, "Meilleur Score 1er", police = "Montserrat", taille= 12, couleur="black")
    texte(110, 145, "2eme", police = "Montserrat", taille= 12, couleur="black")
    texte(410, 180, "3eme", police = "Montserrat", taille= 12, couleur="black")

    texte(100, 205, liste_meilleur[1], police = "Montserrat", taille= 12, couleur="black")
    texte(250, 170, liste_meilleur[0], police = "Montserrat", taille= 12, couleur="black")
    texte(400, 250, liste_meilleur[2], police = "Montserrat", taille= 12, couleur="black")

    attente_clic()
    ferme_fenetre()

def detecter_score(x, y):
    if 120 <= x <= 210 and 565 <= y <= 595:
        return True

def pause(x, y):
    if 260 <= x <= 350 and 565 <= y <= 595:
        return True

def reprendre_ou_quitter():
    x, y, w = attente_clic()
    if 200 <= x <= 400 and 270 <= y <= 320:
        return False    #On considère que false signifie que la partie reprend
    if 200 <= x <= 400 and 340 <= y <= 390:
        return True    #true signifie donc que la partie s'acheve et est sauvegardé

def quitter(liste1, liste2, boolean, n, round, tours, liste_coord_obstacle, nombre_obstacles, sablier, score, version_dynamique, switch_taille_boules, terminaison, obstacles):
    f = "charger.txt"
    f1 = "liste1.txt"
    f2 = "liste2.txt"
    f3 = "jeu.txt"
    f4 = "variantes.txt"
    f5 = "obstacles.txt"
    liste_parametre = [n, round, tours]
    liste_variante = [obstacles, score, version_dynamique, switch_taille_boules, terminaison, sablier]
    liste_obs = [liste_coord_obstacle]
    with open(f1, 'w') as fichier1:
        fichier1.write("")
    with open(f2, 'w') as fichier2:
        fichier2.write("")
    with open(f3, 'w') as fichier3:
        fichier3.write("")
    with open(f4, 'w') as fichier4:
        fichier4.write("")
    with open(f5, 'w') as fichier5:
        fichier5.write("")
    with open(f, "w") as fichier:
        fichier.write(str(boolean))
    with open(f1, 'a') as fichier1:
        fichier1.write("\n")
        for i in range(len(liste1)):
            for j in range(len(liste1[0])):
                chaine_bleu = str(liste1[i][j]) + "\n"
                fichier1.write(chaine_bleu)
    with open(f2, 'a') as fichier2:
        fichier2.write("\n")
        for i in range(len(liste2)):
            for j in range(len(liste2[0])):
                chaine_rouge = str(liste2[i][j]) + "\n"
                fichier2.write(chaine_rouge)
    with open(f3, 'a') as fichier3:
        fichier3.write("\n")
        for i in range(len(liste_parametre)):
            chaine_parametre = str(liste_parametre[i]) + "\n"
            fichier3.write(chaine_parametre)
    with open(f4, 'a') as fichier4:
        fichier4.write("\n")
        for i in range(len(liste_variante)):
            chaine_variantes = str(liste_variante[i]) + "\n"
            fichier4.write(chaine_variantes)
    with open(f5, 'a') as fichier5:
        fichier5.write("\n")
        chaine_obs = str(nombre_obstacles) + "\n"
        fichier5.write(chaine_obs)
        for i in range(len(liste_obs)):
            for j in range(len(liste_obs[0])):
                chaine_obs = str(liste_obs[i][j]) + "\n"
                fichier5.write(chaine_obs)

def sauvegarde(x, y):
    liste_bleu_sauvegarde = []
    liste_bleu_intermediaire = []
    liste_rouge_sauvegarde = []
    liste_rouge_intermediaire = []
    liste_jeu = []
    liste_variantes = []
    liste_obs2 = []
    f1 = "liste1.txt"
    f2 = "liste2.txt"
    f3 = "jeu.txt"
    f4 = "variantes.txt"
    f5 = "obstacles.txt"
    if x > 100 and y > 500 and x < 500 and y < 550:
        with open(f1, 'r') as fichier1:
            lignes = fichier1.readline()
            for lignes in fichier1:
                liste_bleu_intermediaire.append(lignes.split())
            for i in range(0, len(liste_bleu_intermediaire)-3, 4):
                liste_bleu_sauvegarde.append([float(liste_bleu_intermediaire[i][0]), float(liste_bleu_intermediaire[i+1][0]), float(liste_bleu_intermediaire[i+2][0]), float(liste_bleu_intermediaire[i+3][0])])
            for i in range(len(liste_bleu_sauvegarde)):
                cercle(float(liste_bleu_sauvegarde[i][0]), float(liste_bleu_sauvegarde[i][1]), float(liste_bleu_sauvegarde[i][3]), couleur="black", remplissage="blue", epaisseur=3, tag="cerclebleu")
        with open(f2, 'r') as fichier2:
            lignes = fichier2.readline()
            for lignes in fichier2:
                liste_rouge_intermediaire.append(lignes.split())
            for i in range(0, len(liste_rouge_intermediaire)-3, 4):
                liste_rouge_sauvegarde.append([liste_rouge_intermediaire[i][0], liste_rouge_intermediaire[i+1][0], liste_rouge_intermediaire[i+2][0], liste_rouge_intermediaire[i+3][0]])
            for i in range(len(liste_rouge_sauvegarde)):
                cercle(float(liste_rouge_sauvegarde[i][0]), float(liste_rouge_sauvegarde[i][1]), float(liste_rouge_sauvegarde[i][3]), couleur="black", remplissage="red", epaisseur=3, tag="cerclerouge")
        with open(f4, 'r') as fichier4:
            lignes = fichier4.readline()
            for lignes in fichier4:
                liste_variantes.append(lignes.split())
            if liste_variantes[0][0] == 'True':
                obstacles = True
            else:
                obstacles = False
            if liste_variantes[1][0] == 'True':
                score = True
            else:
                score = False
            if liste_variantes[2][0] == 'True':
                version_dynamique = True
            else:
                version_dynamique = False
            if liste_variantes[3][0] == 'True':
                switch_taille_boules = True
            else:
                switch_taille_boules = False
            if liste_variantes[4][0] == 'True':
                terminaison = True
            else:
                terminaison = False
            if liste_variantes[5][0] == 'True':
                sablier = True
            else:
                sablier = False
        with open(f3, 'r') as fichier3:
            lignes = fichier3.readline()
            for lignes in fichier3:
                liste_jeu.append(lignes.split())
            n = int(liste_jeu[0][0])
            compteur_tour = int(liste_jeu[1][0])
            if liste_jeu[2][0] == 'True':
                tours = True
            else:
                tours = False
            
        with open(f5, 'r') as fichier5:
            lignes = fichier5.readline()
            for lignes in fichier5:
                liste_obs2.append(lignes.split())
            nombre_obstacles = int(liste_obs2[0][0])
            if obstacles == True:
                for i in range(1, nombre_obstacles):
                    cercle(int(liste_obs2[i][0][1:-1]), int(liste_obs2[i][1][:-1]), 20, "purple", "purple", epaisseur = 3)

    

#####Code principal#####

if __name__ == '__main__':
    

    largeurfenetre = 600
    hauteurfenetre = 600
    cree_fenetre(largeurfenetre, hauteurfenetre)  #création de la fenetre

    
    n = 1  #On initialise le nombres de tour a 1

    ### création menu : 
    
    ### Titre
    
    rectangle(500, 100, 100, 0,  remplissage='#FDF5E6', tag= "titre")
    texte(200, 30, "Batailes de Boules", police = "Montserrat", taille= 18, tag = "txt1")
    cercle(130, 40, 20, couleur='black', remplissage='blue', epaisseur=2)
    cercle(150, 60, 20, couleur='black', remplissage='red', epaisseur=2)
    cercle(450, 40, 20, couleur='black', remplissage='blue', epaisseur=2)
    cercle(470, 60, 20, couleur='black', remplissage='red', epaisseur=2)

    rectangle(100, 110, 500, 140, remplissage='#FDF5E6')
    texte(250, 115, "Nombres de tours : ", police="Montserrat", taille=15)
    texte(450, 115, n, taille=15, tag="nb_tours")

    rectangle(100, 110, 170, 140, remplissage="#7b706c")
    texte(125, 115, "+", taille=15)
    rectangle(170, 110, 240, 140, remplissage="#7b706c")
    texte(200, 115, "-", taille=15)

    ### premiere variantes dans le menu
    rectangle(275, 200, 100, 150,  remplissage='#FDF5E6', tag= "régle")
    texte(110, 163, "Sablier", police = "Montserrat", taille= 18, tag = "txt1")
    rectangle(275, 200, 250, 150,  remplissage='red', tag= "régle")

    #Autre variantes
    rectangle(500, 200, 325, 150,  remplissage='#FDF5E6', tag= "régle")
    texte(335, 163, "Scores", police = "Montserrat", taille= 18, tag = "txt1")
    rectangle(500, 200, 475, 150,  remplissage='red', tag= "régle")
    
    #Autre variantes
    rectangle(275, 300, 100, 250,  remplissage='#FDF5E6', tag= "régle")
    texte(105, 263, "Tailles Boules", police = "Montserrat", taille= 15, tag = "txt1")
    rectangle(275, 300, 250, 250,  remplissage='red', tag= "régle")

    #Autre variantes
    rectangle(500, 300, 325, 250,  remplissage='#FDF5E6', tag= "régle")
    texte(330, 263, "V. Dynamique", police = "Montserrat", taille= 15, tag = "txt1")
    rectangle(500, 300, 475, 250,  remplissage='red', tag= "régle")
    
    #Autre variantes
    rectangle(275, 400, 100, 350,  remplissage='#FDF5E6', tag= "régle")
    texte(110, 363, "Terminaison", police = "Montserrat", taille= 15, tag = "txt1")
    rectangle(275, 400, 250, 350,  remplissage='red', tag= "régle")

    rectangle(500, 400, 325, 350,  remplissage='#FDF5E6', tag= "régle")
    texte(335, 363 , "Obstacles", police = "Montserrat", taille= 15, tag = "txt1")
    rectangle(500, 400, 475, 350,  remplissage='red', tag= "régle")
    ### JOUER

    rectangle(100, 430, 500, 480,  remplissage='#BDECB6', tag= "titre")
    texte(205, 445 , "NOUVELLE PARTIE", police = "Montserrat", taille= 15, tag = "txt1")

    with open('charger.txt', 'r') as f:
        partie_sauvegarder = f.readline()
        if partie_sauvegarder == 'True':
            rectangle(100, 500, 500, 550,  remplissage='#BDECB6', tag= "titre")
            texte(205, 515 , "CHARGER PARTIE", police = "Montserrat", taille= 15, tag = "txt1")
        else:
            rectangle(100, 500, 500, 550,  remplissage='#FDF5E6', tag= "titre")
            texte(205, 515 , "CHARGER PARTIE", police = "Montserrat", taille= 15, tag = "txt1")
    
    ### FERMER
    rectangle(350, 590, 250 , 560,  remplissage='#FDF5E6', tag= "bouton")
    texte(270, 565, "Fermer", police = "Montserrat", taille= 12, tag = "fermer")

    ### Permet de combiner les variantes et de les activer dans le menu ###
    
    sablier = False
    score = False
    switch_taille_boules = False
    version_dynamique = False
    terminaison = False
    obstacles = False
    while True:
        x, y, w = attente_clic()
        if x > 270 and y > 560 and x < 330 and y < 590:  ### bouton fermer
            ferme_fenetre()

        if x > 100 and y > 150 and x < 275 and y < 200:
            if sablier == False :
                rectangle(250, 150, 275, 200,  remplissage='green', tag= "régle")
                sablier = True
            else:
                rectangle(250, 150, 275, 200,  remplissage='red', tag= "régle")
                sablier = False
        ##### 
        if x > 325 and y > 150 and x < 500 and y < 200:
            if score == False:
                rectangle(475, 150, 500, 200,  remplissage='green', tag= "régle")
                score = True
            else:
                rectangle(475, 150, 500, 200,  remplissage='red', tag= "régle")        
                score = False
        ####
        if x > 100 and y > 250 and x < 275 and y < 300:
            if switch_taille_boules == False:
                rectangle(250, 250, 275, 300,  remplissage='green', tag= "régle")
                switch_taille_boules = True
            else:
                rectangle(250, 250, 275, 300,  remplissage='red', tag= "régle")
                switch_taille_boules = False
       	####
        if x > 325 and y > 250 and x < 500 and y < 300:
       	    if version_dynamique == False:
                rectangle(475, 250, 500, 300,  remplissage='green', tag= "régle")
                version_dynamique = True
            else:
                rectangle(475, 250, 500, 300,  remplissage='red', tag= "régle")
                version_dynamique = False
        ###
        if x > 100 and y > 350 and x < 275 and y < 400:
            if terminaison == False:
                rectangle(250, 350, 275, 400,  remplissage='green', tag= "régle")
                terminaison = True
            else:
                rectangle(250, 350, 275, 400,  remplissage='red', tag= "régle")
                terminaison = False
        
        ####
        if x > 325 and y > 350 and x < 500 and y < 400:
            if obstacles == False:
                rectangle(475, 350, 500, 400,  remplissage='green', tag= "régle")
                obstacles = True
            else:
                rectangle(475, 350, 500, 400,  remplissage='red', tag= "régle")
                obstacles = False

        if x > 100 and y > 110 and x <  170 and y < 140:
            if n < 30:
                n += 1
                efface("nb_tours")
                texte(450, 115, n, taille=15, tag="nb_tours")    #Permet de choisir le nombre de tours souhaiter dans le menu
        if x > 170 and y > 110 and x <  240 and y < 140:
            if n >=2:
                n -= 1
                efface("nb_tours")
                texte(450, 115, n, taille=15, tag="nb_tours")

        if x > 100 and y > 430 and x < 500 and y < 480:
            break
        
        with open('charger.txt', 'r') as f:
            partie_sauvegarder = f.readline()
            if (x > 100 and y > 500 and x < 500 and y < 550) and partie_sauvegarder == 'True':
                break

### Initiation ###
    efface_tout()
    tours = False
    vainqueur = 0
    budget_bleu = 200
    budget_rouge = 200
    surfacebleu = 0
    surfacerouge = 0
    rayon = 0
    liste_bleu = []
    liste_rouge = []
    compteur_tour = 0
    liste_intermediaire = []
    nombre_obstacles = 0
    liste_coord_obstacle = []
    liste_obstacle = []
    
    if obstacles == True and (x > 100 and y > 430 and x < 500 and y < 480):
        nombre_obstacles = randint(2, 6)
        for i in range(nombre_obstacles):
            absc = randint(70, 590)
            ordo = randint(70, 590)
            liste_coord_obstacle.append([absc, ordo])
        for i in range(len(liste_coord_obstacle)-1):
            obst = cercle(liste_coord_obstacle[i][0], liste_coord_obstacle[i][1], 20, "purple", "purple", epaisseur = 3)   #creation des obstacles
            liste_obstacle.append(obst)
    sauvegarde(x, y)

    if terminaison == True:
        rectangle(40, 10, 340, 50,  remplissage='beige', tag= "recbase")
        texte(50, 20, "Terminer le jeu dans 5 tours", couleur = 'black', police = "Montserrat", taille= 15, tag= "textebase") #bouton pour terminer la partie dans 5 tours

# Partie Principale


    while n!= 0:
        efface(round)
        if switch_taille_boules == True:   #affiche le budget de chaque joueur pour la variantes taille_boule
            texte(10, 570, budget_bleu, couleur='blue', police="Montserrat", taille=12, tag="texte_buget_bleu")
            texte(570, 570, budget_rouge, couleur='red', police="Montserrat", taille=12, tag="texte_buget_rouge")
            rectangle(380, 565, 410, 595, couleur="black", remplissage="grey")
            texte(385, 570, "20", couleur="black", taille=15)
            rectangle(420, 565, 450, 595, couleur="black", remplissage="grey")
            texte(425, 570, "40", couleur="black", taille=15)
            rectangle(460, 565, 490, 595, couleur="black", remplissage="grey")
            texte(465, 570, "60", couleur="black", taille=15)
        round = texte(10, 20, compteur_tour, couleur = 'black', police = "Montserrat", taille= 18)   ## Compte le nbres de tours (en haut a gauche)
        rectangle(260, 565, 350, 595, couleur="black", remplissage="beige")
        texte(270, 570, "Pause", couleur="black", taille=18)
        efface("texte_budget_rouge")
        efface("texte_budget_bleu")
        if tours == False:
            txt = texte(370, 20, "C'est au tour du Bleu", couleur = 'blue', police = "Montserrat", taille= 15)  ## Affiche le tour de la personne (c'est au bleu)
            if sablier == True:
                temps = temps_tours(20000) #20 secondes (timer)
            else:
                temps = 100000

            while temps != None:
                if sablier == True:
                    x1, y1, w = temps
                else:
                    x1, y1, w = attente_clic()
                if pause(x1, y1) == True:
                    rectangle(150, 200, 450, 400, couleur="black", remplissage="beige", tag="pause")
                    texte(200, 220, "Le jeu est en pause", couleur="black", taille=18, tag="pause")
                    rectangle(200, 270, 400, 320, couleur="black", remplissage="beige", tag="pause")
                    texte(210, 290, "Reprendre", couleur="black", taille=13, tag="pause")
                    rectangle(200, 340, 400, 390, couleur="black", remplissage="beige", tag="pause")
                    texte(210, 360, "Quitter et sauvegarder", couleur="black", taille=13, tag="pause")
                    action_utilisateur = reprendre_ou_quitter()
                    efface("pause")
                    if action_utilisateur == False:
                        continue
                    if action_utilisateur == True:
                        quitter(liste_bleu, liste_rouge, True, n, compteur_tour, tours, liste_coord_obstacle, nombre_obstacles, sablier, score, version_dynamique, switch_taille_boules, terminaison, obstacles)
                        mise_a_jour()
                        sleep(2)
                        ferme_fenetre()
                if score == True:
                    rectangle(120, 565, 210, 595, couleur="black", remplissage="beige")
                    texte(135, 570, "Score", couleur="black", taille=18)
                    if detecter_score(x1, y1) == True:
                        for i in range(len(liste_bleu)):
                            surfacebleu += (liste_bleu[i][3]**2)*pi
                        for i in range(len(liste_rouge)):
                            surfacerouge += (liste_rouge[i][3]**2)*pi
                        rectangle(80, 160, 300, 350, remplissage='#1b71db', tag="rect_bleu")
                        rectangle(300, 160, 520, 350,  remplissage='#c80c25', tag="rect_rouge")
                        texte(100, 210, ("Voici le score \nactuel de l'equipe\n bleu : ", int(surfacebleu)), police = "Montserrat", taille= 12, couleur="white", tag="score_bleu")
                        texte(325, 210, ("Voici le score \nactuel de l'equipe\n rouge : ", int(surfacerouge)), police = "Montserrat", taille= 12, couleur="white", tag="score_rouge")
                        mise_a_jour()
                        sleep(2)
                        surfacerouge = 0
                        surfacebleu = 0
                        efface("score_bleu")
                        efface("score_rouge")
                        efface("rect_bleu")
                        efface("rect_rouge")
                if terminaison == True:
                    if x1 > 40 and x1 < 315 and y1 > 10 and y1 < 50:    #Pour savoir si on a cliqué sur terminer dans 5 tours
                        n = 5
                        rectangle(200, 180, 400, 350,  remplissage='beige', tag= "rec1")
                        texte(210, 210, " Il reste 5 tours ! \n Vous avez utilisé \n votre tour pour \n le bonus", police = "Montserrat", taille= 14, tag = "txt1")
                        attente_clic()
                        efface("txt1")
                        efface("rec1")
                        efface("textebase")
                        efface("recbase")
                        break     #le tours est alors passé pour celui qui a choisi d'activer le bonus
                if obstacles == True:
                    inter = intersection_obstacle(liste_coord_obstacle, x1, y1, 20)  # permet d'initialiser l'intersection
                    if inter == True:  # si un obstacle est touché alors ca passe au tour suivant (pour les rouges)
                        rectangle(80, 160, 500, 300,  remplissage='beige', tag= "rec1")
                        texte(140, 210, " Obstacle touché !, \n vous passez votre tour", police = "Montserrat", taille= 18, tag = "txt1")
                        attente_clic()
                        efface("txt1")
                        efface("rec1")
                        break
                if switch_taille_boules == True:
                    if 380 <= x1 <= 410 and 565 <= y1 <= 595:
                        rectangle(380, 565, 410, 595, couleur="black", remplissage="green")
                        texte(385, 570, "20", couleur="black", taille=15)
                        rayon = 20
                    if 420 <= x1 <= 450 and 565 <= y1 <= 595:
                        rectangle(420, 565, 450, 595, couleur="black", remplissage="green")
                        texte(425, 570, "40", couleur="black", taille=15)
                        rayon = 40
                    if 460 <= x1 <= 490 and 565 <= y1 <= 595:
                        rectangle(460, 565, 490, 595, couleur="black", remplissage="green")
                        texte(465, 570, "60", couleur="black", taille=15)
                        rayon = 60
                    budget_bleu -= rayon
                else:
                    rayon = 30
                while touche_bord_bleu(x1, y1, rayon) == False :
                    x1, y1, w = attente_clic()
                mise_a_jour()
                inter = intersection_bleu(liste_rouge, x1, y1, rayon)  # permet d'initialiser l'intersection
                if inter == True:  # si il y a une intersection alors ca passe au tour suivant (pour les rouges)
                    rectangle(80, 160, 500, 300,  remplissage='beige', tag= "rec1")
                    texte(140, 210, " Placement Incorrect, \n vous passez votre tour", police = "Montserrat", taille= 18, tag = "txt1")
                    attente_clic()
                    efface("txt1")
                    efface("rec1")
                    break
                elif clic_interieur(liste_rouge, x1, y1) == True:  # si le rouge clique dans le cercle bleu alors il y a un cassage de cercle
                    position = clic_interieur_position(liste_rouge, x1, y1)
                    division_bleu = separation(liste_rouge, x1, y1, surfacerouge, position, "red")
                    liste_rouge.pop(position)
                    cercle_rouge = cercle(division_bleu[0][0][0], division_bleu[0][0][1], division_bleu[0][0][2], "black",  "red", epaisseur = 3, tag="cerclerouge")
                    cercle_rouge2 = cercle(division_bleu[0][1][0], division_bleu[0][1][1], division_bleu[0][1][2], "black",  "red", epaisseur = 3, tag="cerclerouge")
                    liste_rouge.append([division_bleu[0][0][0], division_bleu[0][0][1], cercle_rouge, division_bleu[0][0][2]])
                    liste_rouge.append([division_bleu[0][1][0], division_bleu[0][1][1], cercle_rouge2, division_bleu[0][1][2]])
                    break
                else:
                    cercle_bleu = cercle(x1, y1, rayon, "black",  "blue", epaisseur = 3, tag="cerclebleu")  #sinon ca créer un cercle de couleur bleu
                    liste_bleu.append([x1, y1, cercle_bleu, rayon]) # coordonées des cercles bleu ainsi que leurs rayons s'ajoute sur une liste
                    break
            tours = True #passe au tour des rouges
            if switch_taille_boules == True:   #affiche le budget de chaque joueur pour la variantes taille_boule
                texte(10, 570, budget_bleu, couleur='blue', police="Montserrat", taille=12, tag="texte_buget_bleu")
                texte(570, 570, budget_rouge, couleur='red', police="Montserrat", taille=12, tag="texte_buget_rouge")
                rectangle(380, 565, 410, 595, couleur="black", remplissage="grey")
                texte(385, 570, "20", couleur="black", taille=15)
                rectangle(420, 565, 450, 595, couleur="black", remplissage="grey")
                texte(425, 570, "40", couleur="black", taille=15)
                rectangle(460, 565, 490, 595, couleur="black", remplissage="grey")
                texte(465, 570, "60", couleur="black", taille=15)
            efface(txt)
            if budget_bleu <= 0:  #si le budget tombre a 0 alors il perd la partie
                rectangle(80, 160, 500, 300,  remplissage='beige')
                texte(130, 210, "L'equipe rouge Gagne ! \n Vous n'avez plus de buget", police = "Montserrat", taille= 18)
                attente_clic()
                ferme_fenetre()

        if tours == True:  #meme choses que durant le tour des bleus
            txt = texte(370, 20, "C'est au tour du Rouge", couleur = 'red', police = "Montserrat", taille= 15)
            if sablier == True:
                temps = temps_tours(20000)
            else:
                temps = 10000
            while temps != None:
                if sablier == True:
                    x2, y2, w = temps
                else:
                    x2, y2, w = attente_clic()
                if pause(x2, y2) == True:
                    rectangle(150, 200, 450, 400, couleur="black", remplissage="beige", tag="pause")
                    texte(200, 220, "Le jeu est en pause", couleur="black", taille=18, tag="pause")
                    rectangle(200, 270, 400, 320, couleur="black", remplissage="beige", tag="pause")
                    texte(210, 290, "Reprendre", couleur="black", taille=13, tag="pause")
                    rectangle(200, 340, 400, 390, couleur="black", remplissage="beige", tag="pause")
                    texte(210, 360, "Quitter et sauvegarder", couleur="black", taille=13, tag="pause")
                    action_utilisateur = reprendre_ou_quitter()
                    efface("pause")
                    if action_utilisateur == False:
                        continue
                    if action_utilisateur == True:
                        quitter(liste_bleu, liste_rouge, True, n, compteur_tour, tours, liste_coord_obstacle, nombre_obstacles, sablier, score, version_dynamique, switch_taille_boules, terminaison, obstacles)
                        mise_a_jour()
                        sleep(2)
                        ferme_fenetre()
                if score == True:
                    rectangle(120, 565, 210, 595, couleur="black", remplissage="beige")
                    texte(135, 570, "Score", couleur="black", taille=18)
                    if detecter_score(x2, y2) == True:
                        for i in range(len(liste_bleu)):
                            surfacebleu += (liste_bleu[i][3]**2)*pi
                        for i in range(len(liste_rouge)):
                            surfacerouge += (liste_rouge[i][3]**2)*pi
                        rectangle(80, 160, 300, 350, remplissage='#1b71db', tag="rect_bleu")
                        rectangle(300, 160, 520, 350,  remplissage='#c80c25', tag="rect_rouge")
                        texte(100, 210, ("Voici le score \nactuel de l'equipe\n bleu : ", int(surfacebleu)), police = "Montserrat", taille= 12, couleur="white", tag="score_bleu")
                        texte(325, 210, ("Voici le score \nactuel de l'equipe\n rouge : ", int(surfacerouge)), police = "Montserrat", taille= 12, couleur="white", tag="score_rouge")
                        mise_a_jour()
                        sleep(2)
                        surfacebleu = 0
                        surfacerouge = 0
                        efface("score_bleu")
                        efface("score_rouge")
                        efface("rect_bleu")
                        efface("rect_rouge")
                if terminaison == True:
                    if x2 > 40 and x2 < 315 and y2 > 10 and y2 < 50:
                        n = 5
                        rectangle(200, 180, 400, 350,  remplissage='beige', tag= "rec1")
                        texte(210, 210, " Il reste 5 tours ! \n Vous avez utilisé \n votre tour pour \n le bonus", police = "Montserrat", taille= 18, tag = "txt1")
                        attente_clic()
                        efface("txt1")
                        efface("rec1")
                        efface("textebase")
                        efface("recbase")
                        break
                if obstacles == True:
                    inter = intersection_obstacle(liste_coord_obstacle, x2, y2, 20)
                    if inter == True:
                        rectangle(80, 160, 500, 300,  remplissage='beige', tag= "rec1")
                        texte(140, 210, " Obstacle touché !, \n vous passez votre tour", police = "Montserrat", taille= 18, tag = "txt1")
                        attente_clic()
                        efface("txt1")
                        efface("rec1")
                        break
                if switch_taille_boules == True:
                    if 380 <= x2 <= 410 and 565 <= y2 <= 595:
                        rectangle(380, 565, 410, 595, couleur="black", remplissage="green")
                        texte(385, 570, "20", couleur="black", taille=15)
                        rayon = 20
                    if 420 <= x2 <= 450 and 565 <= y2 <= 595:
                        rectangle(420, 565, 450, 595, couleur="black", remplissage="green")
                        texte(425, 570, "40", couleur="black", taille=15)
                        rayon = 40
                    if 460 <= x2 <= 490 and 565 <= y2 <= 595:
                        rectangle(460, 565, 490, 595, couleur="black", remplissage="green")
                        texte(465, 570, "60", couleur="black", taille=15)
                        rayon = 60
                    budget_rouge -= rayon
                else:
                    rayon = 30
                while touche_bord_bleu(x2, y2, rayon) == False :
                    x2, y2, w = attente_clic()
                mise_a_jour()
                inter = intersection_rouge(liste_bleu, x2, y2, rayon)
                if inter == True:
                    rectangle(80, 160, 500, 300,  remplissage='beige', tag= "rec1")
                    texte(140, 210, " Placement Incorrect, \n vous passez votre tour", police = "Montserrat", taille= 18, tag = "txt1")
                    attente_clic()
                    efface("txt1")
                    efface("rec1")
                    break
                elif clic_interieur(liste_bleu, x2, y2) == True:
                    position = clic_interieur_position(liste_bleu, x2, y2)
                    division_rouge = separation(liste_bleu, x2, y2, surfacebleu, position, "blue")
                    liste_bleu.pop(position)
                    cercle_bleu = cercle(division_rouge[0][0][0], division_rouge[0][0][1], division_rouge[0][0][2], "black",  "blue", epaisseur = 3, tag="cerclebleu")
                    cercle_bleu2 = cercle(division_rouge[0][1][0], division_rouge[0][1][1], division_rouge[0][1][2], "black",  "blue", epaisseur = 3, tag="cerclebleu")
                    liste_bleu.append([division_rouge[0][0][0], division_rouge[0][0][1], cercle_bleu, division_rouge[0][0][2]])
                    liste_bleu.append([division_rouge[0][1][0], division_rouge[0][1][1], cercle_bleu2, division_rouge[0][1][2]])
                    break
                else:
                    cercle_rouge = cercle(x2, y2, rayon, "black",  "red", epaisseur = 3, tag="cerclerouge")
                    liste_rouge.append([x2, y2, cercle_rouge, rayon])
                    break
            tours = False
            efface(txt)
            if budget_rouge <= 0:
                rectangle(80, 160, 500, 300,  remplissage='beige')
                texte(130, 210, "L'equipe bleu Gagne ! \n Vous n'avez plus de buget", police = "Montserrat", taille= 18)
                attente_clic()
                ferme_fenetre()
        if version_dynamique == True:  #On ajoute le rayon au cercles poser precedemment et on doit changer les listes pour garder en memoire le nouveau rayon
            liste_intermediaire = []
            rayon_grandb = rayon_grandi(liste_bleu, liste_rouge)
            efface("cerclebleu")
            for i in range(len(rayon_grandb)):
                cercle(rayon_grandb[i][0], rayon_grandb[i][1], rayon_grandb[i][3], "black", "blue", epaisseur=3)
                liste_intermediaire.append(rayon_grandb[i])
            liste_bleu = []
            for i in range(len(liste_intermediaire)):
                liste_bleu.append(liste_intermediaire[i])
        if version_dynamique == True:
            liste_intermediaire = []
            rayon_grandr = rayon_grandi(liste_rouge, liste_bleu)
            efface("cerclerouge")
            for i in range(len(rayon_grandr)):
                cercle(rayon_grandr[i][0], rayon_grandr[i][1], rayon_grandr[i][3], "black", "red", epaisseur=3)
                liste_intermediaire.append(rayon_grandr[i])
            liste_rouge = []
            for i in range(len(liste_intermediaire)):
                liste_rouge.append(liste_intermediaire[i])
        n -= 1  #On enleve 1 au tour
        compteur_tour += 1  #permet de rajouter le numero du round (ex : 1, 2, 3, 4) (en haut a droite de la fenetre)
        efface(round)
        efface("texte_budget_rouge")
        efface("texte_budget_bleu")
        mise_a_jour()
    for i in range(len(liste_bleu)):
        surfacebleu += (liste_bleu[i][3]**2)*pi
    for i in range(len(liste_rouge)):
        surfacerouge += (liste_rouge[i][3]**2)*pi
    with open("charger.txt", "w") as fichier:
        fichier.write("False")
    ecran_fin_de_jeu(surfacebleu, surfacerouge)
    