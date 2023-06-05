# Python-Boules-Game

----- Consigne -----

Le but de ce projet est de réaliser un jeu de placement de boules. Chaque utilisateur joue
avec une couleur. Le but du jeu est d’occuper la plus grande aire coloriée avec sa couleur. Les
joueurs contrôlent la souris chacun à leur tour, et on décide à l’avance du nombre de tours.

Jeu de Base : 

1) Les intérieurs de deux boules de couleurs différentes ne peuvent pas s’intersecter. Si
un joueur essaye d’inclure une boule qui intersecte l’intérieur d’une boule de la couleur
opposée, rien ne se passe et il perd son tour.

2) Si un joueur clique dans l’intérieur d’une boule de l’adversaire, il la transforme en deux
boules de même couleur plus petites. Une des deux boules a pour centre l’endroit où l’on
a cliqué, et est tangente à la boule d’origine, et l’autre est tangente à la boule d’origine et
à la nouvelle boule. 

Fonctionalités 

1. Sablier : chaque joueur a un temps prédéterminé pour jouer à chaque tour ; s’il ne réagit
pas à temps, il perd son tour.
2. Scores : un joueur peut vérifier quelle aire ses boules totalisent à chaque instant en
appuyant sur la touche ’s’. On affiche le score pour les deux joueurs, et il disparaît après
2 secondes.
3. Taille des boules : à chaque tour, on demande au joueur le rayon de la boule qu’il veut
introduire. Il commence avec un certain budget fixé au préalable, et pour chaque boule
posée, son budget diminue du rayon de la boule qu’il pose.
4. Version dynamique : les rayons de toutes les boules s’incrémentent à chaque tour en
respectant les règles données (dès que deux boules de couleurs différentes se touchent,
elles arrêtent de grandir).
5. Terminaison : ajouter une règle permettant à un joueur de décider une fois par partie
que le jeu se termine dans 5 tours.
6. Obstacles : le tableau commence avec certains obstacles que les boules ne peuvent pas
toucher. Vous pouvez décider du type et de la forme des obstacles.

Pour finir il y a également une sauvegarde du jeu (on peut récuperer notre ancienne sauvegarde pour 
jouer à notre sauvegarde précédente.


Notre Read Me : 

----- La Bataille des Boules -----

par Guerreiro Noah et Vivier Matis

Le jeu se joue en tour par tour et le but est de remplir 
le plus de surface possible avec vos cercles en cliquant 
sur la position voulue. Il y a un nombre de tours ‡ 
implÈmenter et ‡ la fin des tours, celui ou celle avec le
plus de cercles remportent la partie.

----- infos utilisateur -----

Vous ne pouvez pas cliquer trop proche de la boule de l'adversaire
(passe votre tour si cela se produit)
Vous ne pouvez pas cliquer sur votre propre cercle
(passe votre tour si cela se produit)
Vous pouvez en revanche cliquer sur la boule de votre adversaire
qui se verra rÈduire en taille.
Vous l'avez compris, vous pouvez rÈduire la surface de votre adversaire
en cliquant sur sa boule, en revanche vous ne pouvez pas rÈduire sa boule
et vous mÍme posez votre boule
Il y a des limites de la zone de jeu, vous ne pouvez pas cliquer
trop prÍt des limites (passe votre tour si cela se produit)
Si les limites de bordures sont atteintes, un message d'erreur
apparait et le tour du joueur doit etre recommencer.
Si vous prenez plus de 20 secondes pour cliquer, 
votre tours passe.
Il y a diffÈrents modes de jeu accessibles sur le menu avant de lancer le jeu.
Je vous laisse dÈcouvrir et tester par vous mÍme tous les modes disponibles.

IMPORTANT : Pour que la sauvegarde fonctionne, il faut se placer dans le repertoire
ou il y a le fichier main.py ainsi que les fichiers qui contiennent les diffÈrentes 
donnÈes sauvegardÈes du jeu.

----- DisponibilitÈ ------

Voici une liste de toutes les choses disponibles dans notre jeu
- Permet de choisir le nombres de tour que nous voulons jouer (au menu)
- Des bordures empechant les cercles de se crÈer
- L'intersection
- Un compteur de tour
- Voir si c'est au tour des bleus ou des rouges
- Affiche le gagnant
- La division du cercle adverse
- un menu
- variantes : 
	sablier
	taille des boules
	version dynamique
	terminaison
	obstacles
	scores
- bonus :
	classement
	pause et sauvegarde
