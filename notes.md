# Planning

## Par Jeanne Martinet et Valentin Paolicelli

# Présentation des fonctionnalités 

Un site en Flask permettant de planifier le menu de la semaine. 
Il faut être capable de choisir les repas pour le midi et le soir. 
Il faut pouvoir ajouter des repas à la listes des repas et préciser les ingrédients.
Il faudrait pouvoir accéder à une liste d'ingrédient et aussi rajouter des ingrédients.
Préciser le nombre de personne mangeant à ces repas ainsi que qui sont ces personnes : Jeanne, Valentin, Default.
Il faut pouvoir préciser les stocks actuellement présent.
La liste de course précise exactement ce qu'il faut acheter et précise aussi les stocks restant à la fin de la semaine si tout se déroule comme prévu.
On pourrait avoir une fonctionnalité pour clicker sur un jour et voir ce que l'on mange, et ce qu'il reste en stock à la fin de la journée ainsi que ce que l'on consomme dans la journée.
Une fonctionnalité pour prévoir le coût de la semaine.
Si on fait le coût il faudrait aussi prendre en compte les alternatives, 1kg de pate ou les poivrons.
Si on attribue une recette longue à un slot cours prévention !
Il faudrait savoir le jour ou on est et faire un debrief de si on a bien suivi ce qui était dit dans l'emploi du temps et d'effectuer les modifications sinon. 
Préciser si on a cours ou non et préciser les horaires avec les horaires classiques par défaut.

Ingrédient :  Prix, sa quantité (s'achète par tant), unité de mesure
Recette : Ingrédients, Quantité de chaque ingrédient,
Recettes : Liste des recettes, prix, longue ou courte, utilisateur
Jour : 2 recettes, 2 case cours
Semaine : 7 jours

# Les différentes routes de l'application

Il faut une page main = menu et affichant le programme de la semaine.
On peut naviguer de semaine en semaine.
On peut modifier le programme ce qui emmene sur la page planning
Une page ajouter un ingrédient
Une page ajouter une recette
