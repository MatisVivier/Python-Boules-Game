----- La Bataille des Boules -----

par Guerreiro Noah et Vivier Matis

Le jeu se joue en tour par tour et le but est de remplir 
le plus de surface possible avec vos cercles en cliquant 
sur la position voulue. Il y a un nombre de tours � 
impl�menter et � la fin des tours, celui ou celle avec le
plus de cercles remportent la partie.

----- infos utilisateur -----

Vous ne pouvez pas cliquer trop proche de la boule de l'adversaire
(passe votre tour si cela se produit)
Vous ne pouvez pas cliquer sur votre propre cercle
(passe votre tour si cela se produit)
Vous pouvez en revanche cliquer sur la boule de votre adversaire
qui se verra r�duire en taille.
Vous l'avez compris, vous pouvez r�duire la surface de votre adversaire
en cliquant sur sa boule, en revanche vous ne pouvez pas r�duire sa boule
et vous m�me posez votre boule
Il y a des limites de la zone de jeu, vous ne pouvez pas cliquer
trop pr�t des limites (passe votre tour si cela se produit)
Si les limites de bordures sont atteintes, un message d'erreur
apparait et le tour du joueur doit etre recommencer.
Si vous prenez plus de 20 secondes pour cliquer, 
votre tours passe.
Il y a diff�rents modes de jeu accessibles sur le menu avant de lancer le jeu.
Je vous laisse d�couvrir et tester par vous m�me tous les modes disponibles.

IMPORTANT : Pour que la sauvegarde fonctionne, il faut se placer dans le repertoire
ou il y a le fichier main.py ainsi que les fichiers qui contiennent les diff�rentes 
donn�es sauvegard�es du jeu.

----- Disponibilit� ------

Voici une liste de toutes les choses disponibles dans notre jeu
- Permet de choisir le nombres de tour que nous voulons jouer (au menu)
- Des bordures empechant les cercles de se cr�er
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

Voici une liste de toutes les erreurs du jeu (choses impossible � faire) :
- Divisions impossible lors du mode version dynamique et taille des boules est activer
- Les touches ne fonctionnes pas (il faut appuyer sur l'�cran pour voir le score et activer le mode terminaison)

----- D�roulement du Projet -----

Nous avons programmer ce projet � deux avec une r�partition des taches. 

- cr�ation fenetre
- ajout du tour par tour
- cr�ation des lites avec toutes les info n�cessaires a afficher
- calcul du score
- impl�mentation intersection
- cr�ation bordures
- impl�mentation division
- Ajout du timer
- cr�ation du menu
- ajouts des variantes
- ajouts des bonus

Nous avions chacun une tache � r�aliser et si une personne finisait et que l'autre
n'y arrivait pas, nous collaborions.



----- Probl�mes rencontrer ------

Nous avons rencontrer certains probl�mes qui nous ont pris quelques heures
� r�soudre, voici une liste des probl�mes avec leur solutions :

- L'intersection : Nous n'arrivions pas � faire l'intersection entre deux cercles.
Notre programmes � l'origine consister � empecher de faire un cercle trop proche 
du cercle adverse (le but de l'intersection). Elle marchait bien car une fois que
le joueur 2 cliquez trop proche du cercle mis auparavant du joueur 1, le cercle 
rouge ne se dessinez pas. Mais le probl�me �tait que les coordonn�es cliquer par 
le joueur 2 �tait sauvegardez (comme un cercle invisible) et il �tait impossible
de construire un cercle par le joueur 1 quand il cliquer pr�t des anciennes
coordon�es du joueur 2. 

--> La solution � �t� de cr�er deux Fonctions 'intersection_bleu' et 
'intersection_rouge' qui cr�er tout les deux des listes pour les 
coordon�es rouge et bleu et �viter l'intersection entres toutes les 
coordon�es sur les deux listes. Cela permet d'�viter de toujours garder 
les coordon�es pr�cedentes mais de pouvoir naviguer sur les deux listes et donc
d'avoir acc�s � toutes les coordon�es cliquer sur l'espace de jeu

- Le 'split' : Le 'split', autrement le cassage de cercle de l'adversaire
� �t� une grosse probl�matique (nous avons pass� plus de dix heures sur cette
partie). Quand on �xecute le programme, que l'on place un cercle bleu, un 
cercle rouge, un autre cercle bleu et que ensuite pendant le tour du joueur
rouge on clique sur le joueur bleu, le 'split' se fait sans aucun probl�me
quand nous placons un autre cercle bleu et ensuite que nous essayons de 
casser ce nouveau cercle pendant le tour du rouge, cela ne marche plus. Nous 
avons essayer toutes les combinaisons et ca ne marche toujours pas. Ensuite, 
toujours dans le meme dommaines, quand nous voulons cliquer sur le cercle rouge
en tant que joueur bleu, seul un petit point se cr�er. Pour finir, toujours dans le 
meme domaine, lors du quatri�me tour (c'est un exemple), il est impossible pour le joueur
rouge de casser le cercle bleu poser durant le premier tour. Sinon, un grand cercle se 
produit et le cercle bleu disparait. 
Lors du second rendu, nous avions r�gler le probl�me avec la division mais quand nous 
avons rajouter des variantes, la division ne marchait pas quand nous lancions les variantes
tailles des boules ou la version dynamique. 

- L'affichage de la variante score qui ne fonctionne pas quand on presse une touche

 

