# Partie 1 : la bataille navale

Nous allons créer un moteur de jeu minimaliste de bataille navale. Les navires que nous allons créer vont pouvoir se tirer dessus et s’infliger des dégâts, le but étant de terminer la partie avec le moins de dégâts possible.

Dans cette première partie, nous allons considérer que tous les navires sont des navires de guerre.

## Exercice 1

Créer une classe Navire.

Un navire possède, au minimum : un nom, un fabriquant, une année de construction, une longueur, une puissance moteur, une couleur, un kilométrage.

Étant donné qu’il s’agit de navires de guerre, on indiquera également une puissance de tir, une résistance (ce sont des float de 0 à 100, 0 = faible, 100 = fort), et des points de vie correspondant à l’état du navire (un float de 0 à 100, 100 = aucun dégât, 0 = navire détruit). On ne vérifie pas la validité des valeurs.

Créer le constructeur pour la classe Navire.

## Exercice 2

L’état du navire doit être déterminé par le nombre de points de vie. 

Deux états possibles : le navire est détruit (si les points de vie sont nuls) ou non.

## Exercice 3
Créer une méthode permettant de retourner les informations d’un navire, de sorte que lorsque l’on fait un print() sur une instance de Navire, elles s’affichent sous cette forme :

[ NOM - FABRIQUANT (Année) ]\
Longueur mètres - PuissanceMoteur ch\
Couleur - kilométrage NM\
Puissance de tir : XXX\
Résistance : XXX\
Points de vie : XXX/100\
Etat : En marche ou Détruit

Par exemple pour un navire nommé «Le titan», fabriqué par «Naval Group» en 2015, long de 50 mètres, une puissance moteur de 8000 ch, de couleur grise, avec 450000 NM navigués, une puissance de tir de 75 points, une résistance de 60 points et une jauge de points de vie maximale:

[ LE TITAN – NAVAL GROUP (2015) ]\
50 mètres - 8000 ch\
Gris - 450000 NM\
Puissance de tir : 75.0\
Résistance : 60.0\
Points de vie : 100/100\
Etat : En marche 
 

## Exercice 4

Dans le main du programme, créer plusieurs navires différents (au moins trois) et afficher leurs informations.

## Exercice 5

Ajouter une méthode naviguer(), qui prend en paramètre un certain nombre de milles (il s’agit de l’unité de mesure utilisée en mer, 1 mille = 1,852 km).

Naviguer aura donc pour effet d’augmenter le kilométrage.

À chaque déplacement, afficher dans la console (N1 correspond au nom du navire qui navigue) :

N1 navigue.\
xxxx NM parcourus.\
Kilométrage actuel : xxxxx NM.\

## Exercice 6

Ajouter une méthode subir_degats(), qui prend un paramètre un certain nombre.

Il faudra déduire ce nombre passé en paramètre aux points de vie. Les points de vie ne peuvent pas être négatifs.
Pour rappel un navire dont les points de vie sont nuls est détruit.


## Exercice 7

Ajouter une méthode tirer_sur(), qui prend un paramètre correspondant à un navire ennemi. Tirer sur un navire aura pour effet de faire subir des dégâts à ce navire.

Ce niveau de dégâts sera déterminé par :
- la puissance de tir du navire qui tire ;
- la résistance du navire qui subit le tir ;
- un facteur aléatoire.

Voici la formule :

Dégâts infligés = (((0,5 + random1) * puissance de tir) - (random2 * résistance)) * random3

random1, random2 et random3 sont trois nombres aléatoires différents.

Pour générer un nombre aléatoire, on utilise la fonction random.random() (il faudra indiquer import random en première ligne du fichier).

Utiliser la fonction round() pour arrondir le résultat.

Si le résultat du calcul est nul ou négatif, on considère que le tir a échoué, on n’inflige alors aucun dégât.

## Exercice 8
Un navire perd 5 points de résistance à chaque tir subi.

Si le navire ennemi (N2) est détruit suite à un tir, afficher un message dans la console pour l’indiquer.

Un navire perd 1 point de puissance de tir à chaque tir (réussi ou non).

Un navire qui tire sur un navire déjà détruit rate systématiquement son tir.

À chaque tir, afficher dans la console (N1 correspond au tireur, N2 la victime du tir) :

N1 tire sur N2.\
xx dégâts infligés ou Le tir a échoué !\
Puissance N1 = xx.\
Résistance N2 = xx.\
Points de vie N2 = xxx/100.\

Pour rappel, la puissance de tir et la résistance ne peuvent être négatifs.

# Partie 2: les navires se complexifient 

Nous allons créer de nouvelles classes, qui vont permettre de découpler certaines informations d’un navire. Cela nécessitera des modifications structurelles au niveau de la classe précédemment créée.

## Exercice 9
En réalité, un navire est plus complexe que cela. Il possède une coque, et des armes.

Créer une classe Coque, qui possède une résistance, des points de vie, une matière et une couleur. Supprimer les attributs redondants dans la classe Navire.

Créer une classe Arme, qui possède un nom, une puissance de tir et un prix. Supprimer les redondances dans la classe Navire. Pour le moment, un navire ne possède qu’une seule arme.

Adapter / déplacer les méthodes existantes si nécessaire.

Dans la méthode permettant d’afficher les informations d’un navire, remplacer l’affichage de la couleur, puissance de tir, résistance et points de vie par les informations sur la coque et l’arme.

## Exercice 10
Dans le main, adapter les navires existants suite aux modifications.

Chaque navire doit se déplacer 3 fois et parcourir 2000 NM au minimum. Chaque navire doit avoir subi au moins un tir, et tirer au moins une fois sur chaque navire (si son état le permet).

Afficher les informations de chaque navire à la fin du programme.

# Partie 3: des navires de guerre et des navires civils

Dans cette partie, nous allons considérer que la classe Navire va servir de base (classe abstraite) pour la création de deux classes : les navires de guerre, qui peuvent tirer ; et les navires civils … qui ne peuvent pas.

## Exercice 11
Nous allons distinguer deux types de navires : les navires de guerre et les navires civils.

Les navires de guerre sont des navires normaux auxquels on a ajouté une arme. Seuls les navires de guerre peuvent tirer sur d’autres navires.

Créer une classe NavireDeGuerre qui hérite de Navire.

## Exercice 12

Créer une classe NavireCivil, qui hérite de Navire.

Un navire civil est principalement destiné au tourisme, il possède un nombre de passagers, une capacité de passagers maximale, et une liste de destinations (facultatif).

Un navire civil ne peut bien entendu pas tirer. Il peut en revanche déposer des passagers, et en récupérer des nouveaux, dans la limite de sa capacité maximale.

## Exercice 13

Empêcher un navire de guerre de tirer sur lui-même (il ne perd pas de point de puissance de tir dans ce cas-là).

Lorsqu’un navire de guerre tire sur un navire civil ou navire médical, le navire de guerre perd 10 points de dégâts et 10 points de puissance de tir.

## Exercice 14

Créer des classes d’exception, correspondantes aux différentes exceptions susceptibles d’être levées dans le programme.
Par exemple, lorsque l’on tente de créer un navire avec une puissance supérieure à 100, ou bien encore lorsqu’un navire détruit tente de se déplacer ou tirer.

# Partie 4: sauvegarde des navires

Dans cette dernière partie, nous allons mettre en place de la persistance de données, grâce aux librairies CSV et JSON.

## Exercice 15

Grâce à la librairie csv, ajouter une méthode dans NavireDeGuerre qui sauvegarde toutes les informations d’un navire sous la forme d’un CSV.

Le nom du fichier CSV doit être de la forme « navire_<nom du navire>.csv ».


## Exercice 16
Grâce au module json, ajouter une méthode dans NavireDeGuerre qui sauvegarde toutes les informations d’un navire sous la forme d’un JSON.

Le nom du fichier CSV doit être de la forme « navire_<nom du navire>.json ». 

Ajouter également une méthode qui permet de recréer un navire à partir d’une sauvegarde JSON précédente.
