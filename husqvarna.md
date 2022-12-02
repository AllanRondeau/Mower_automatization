# **Husqvarna**

*Dernière modification le 10/01/2020*

## **Préambule**

La société *Husqvarna* développe une tondeuse à gazon automatique capable de tondre des surfaces rectangulaires.  
Cette tondeuse peut être programmée pour parcourir l'intégralité de la surface.

La position de la tondeuse est représentée par une combinaison de coordonnées **x, y** et d'une lettre indiquant l'orientation selon la notation cardinale anglaise : **N, E, S, W**. La pelouse est divisée en grille pour simplifier la navigation.  
Par exemple, la position de la tondeuse **00 N** signifie qu'elle se situe dans le coin inférieur gauche de la pelouse, et qu'elle est orientée vers le nord.

Pour contrôler la tondeuse, on lui envoie une séquence simple de lettres. Les lettres possibles sont **D**, **G** et **A**.  
* **D** et **G** font pivoter la tondeuse de 90° à droite ou à gauche respectivement, sans la déplacer.
* **A** signifie que l'on avance la tondeuse d'une case dans la direction à laquelle elle fait face, sans modifier son orientation.

Si la position après mouvement est en dehors de la pelouse, la tondeuse ne bouge pas, conserve son orientation et traite la commande suivante.

Chaque tondeuse se déplace de façon séquentielle, ce qui signifie que la seconde tondeuse ne bouge que lorsque la première e exécuté intégralement sa série d'instructions.  
Lorsqu'une tondeuse achève sa série d'instructions, elle communique sa position et son orientation.

Pour programmer l'exploration, on fournit un fichier construit comme suit : 
* La première ligne correspond aux coordonnées du coin supérieur droit de la pelouse, celles du coin supérieur gauche sont supposées être **0, 0**.
* La suite du fichier permet de piloter toutes les tondeuses qui ont été déployées. Chaque tondeuse a deux lignes la concernant :
    * La première ligne donne la position initiale de la tondeuse, ainsi que son orientation. La position et l'orientation sont fournis sous la forme de 2 chiffres et 1 lettre, séparés par un espace.
    * La seconde ligne est un série d'instructions ordonnant à la tondeuse d'explorer la pelouse. Les instructions sont une suite de caractères sans espaces.

## **Objectif**

Concevoir et écrire un programme implémentant les spécifications ci-dessus.

#### Fichier en entrée

Le programme recevra en entrée un fichier dont le contenu est le suivant :

> 55  
44 S  
GADDAAGADAA  
22 N  
AADGGDADGA  

#### Résultat attendu

La position finale des tondeuses devra être la suivante :
>13 W  
25 N

## **Bonus**

Créer un fork de votre premier algorithme, pour y apporter tous les axes d'amélioration que vous jugerez nécessaires.  
Ces améliorations devront être spécifiées et commentées dans un fichier externe.
