# Python-Boules-Game

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
