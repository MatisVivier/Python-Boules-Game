----- La Bataille des Boules -----

par Guerreiro Noah et Vivier Matis

Le jeu se joue en tour par tour et le but est de remplir 
le plus de surface possible avec vos cercles en cliquant 
sur la position voulue. Il y a un nombre de tours à 
implémenter et à la fin des tours, celui ou celle avec le
plus de cercles remportent la partie.

----- infos utilisateur -----

Vous ne pouvez pas cliquer trop proche de la boule de l'adversaire
(passe votre tour si cela se produit)
Vous ne pouvez pas cliquer sur votre propre cercle
(passe votre tour si cela se produit)
Vous pouvez en revanche cliquer sur la boule de votre adversaire
qui se verra réduire en taille.
Vous l'avez compris, vous pouvez réduire la surface de votre adversaire
en cliquant sur sa boule, en revanche vous ne pouvez pas réduire sa boule
et vous même posez votre boule
Il y a des limites de la zone de jeu, vous ne pouvez pas cliquer
trop prêt des limites (passe votre tour si cela se produit)
Si les limites de bordures sont atteintes, un message d'erreur
apparait et le tour du joueur doit etre recommencer.
Si vous prenez plus de 20 secondes pour cliquer, 
votre tours passe.
Il y a différents modes de jeu accessibles sur le menu avant de lancer le jeu.
Je vous laisse découvrir et tester par vous même tous les modes disponibles.

IMPORTANT : Pour que la sauvegarde fonctionne, il faut se placer dans le repertoire
ou il y a le fichier main.py ainsi que les fichiers qui contiennent les différentes 
données sauvegardées du jeu.

----- Disponibilité ------

Voici une liste de toutes les choses disponibles dans notre jeu
- Permet de choisir le nombres de tour que nous voulons jouer (au menu)
- Des bordures empechant les cercles de se créer
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

----- Erreurs -------

Voici une liste de toutes les erreurs du jeu (choses impossible à faire) :
- Divisions impossible lors du mode version dynamique et taille des boules est activer
- Les touches ne fonctionnes pas (il faut appuyer sur l'écran pour voir le score et activer le mode terminaison)

----- Déroulement du Projet -----

Nous avons programmer ce projet à deux avec une répartition des taches. 

- création fenetre
- ajout du tour par tour
- création des lites avec toutes les info nécessaires a afficher
- calcul du score
- implémentation intersection
- création bordures
- implémentation division
- Ajout du timer
- création du menu
- ajouts des variantes
- ajouts des bonus

Nous avions chacun une tache à réaliser et si une personne finisait et que l'autre
n'y arrivait pas, nous collaborions.



----- Problèmes rencontrer ------

Nous avons rencontrer certains problèmes qui nous ont pris quelques heures
à résoudre, voici une liste des problèmes avec leur solutions :

- L'intersection : Nous n'arrivions pas à faire l'intersection entre deux cercles.
Notre programmes à l'origine consister à empecher de faire un cercle trop proche 
du cercle adverse (le but de l'intersection). Elle marchait bien car une fois que
le joueur 2 cliquez trop proche du cercle mis auparavant du joueur 1, le cercle 
rouge ne se dessinez pas. Mais le problème était que les coordonnées cliquer par 
le joueur 2 était sauvegardez (comme un cercle invisible) et il était impossible
de construire un cercle par le joueur 1 quand il cliquer prêt des anciennes
coordonées du joueur 2. 

--> La solution à été de créer deux Fonctions 'intersection_bleu' et 
'intersection_rouge' qui créer tout les deux des listes pour les 
coordonées rouge et bleu et éviter l'intersection entres toutes les 
coordonées sur les deux listes. Cela permet d'éviter de toujours garder 
les coordonées précedentes mais de pouvoir naviguer sur les deux listes et donc
d'avoir accés à toutes les coordonées cliquer sur l'espace de jeu

- Le 'split' : Le 'split', autrement le cassage de cercle de l'adversaire
à été une grosse problématique (nous avons passé plus de dix heures sur cette
partie). Quand on éxecute le programme, que l'on place un cercle bleu, un 
cercle rouge, un autre cercle bleu et que ensuite pendant le tour du joueur
rouge on clique sur le joueur bleu, le 'split' se fait sans aucun problème
quand nous placons un autre cercle bleu et ensuite que nous essayons de 
casser ce nouveau cercle pendant le tour du rouge, cela ne marche plus. Nous 
avons essayer toutes les combinaisons et ca ne marche toujours pas. Ensuite, 
toujours dans le meme dommaines, quand nous voulons cliquer sur le cercle rouge
en tant que joueur bleu, seul un petit point se créer. Pour finir, toujours dans le 
meme domaine, lors du quatrième tour (c'est un exemple), il est impossible pour le joueur
rouge de casser le cercle bleu poser durant le premier tour. Sinon, un grand cercle se 
produit et le cercle bleu disparait. 
Lors du second rendu, nous avions régler le problème avec la division mais quand nous 
avons rajouter des variantes, la division ne marchait pas quand nous lancions les variantes
tailles des boules ou la version dynamique. 

- L'affichage de la variante score qui ne fonctionne pas quand on presse une touche

 

