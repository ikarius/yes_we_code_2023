# Présentation du projet

**Voici un lien vers la vidéo du projet : <https://youtu.be/8GVUnEX_JdE>**

Nous avons décidé de télécommander un **Rover Freenove** qui est un petit robot a roulette (voir vidéo ici : <https://www.youtube.com/watch?v=H7P5lZo29lA>) avec une carte microBit et de lui faire dessiner différentes figures et faire une petite danse pour se reposer.

Nous avons décidé de tracer les différentes formes sur un papier avec un stylo accroché au rover, mais tout ne s'est passé comme prévu (pour le triangle et le carré).

Pour le cercle tout a bien marché.

Le rover a besoin d'une carte microBit pour fonctionner. Il nous a donc fallu 2 cartes :
- une pour la télécommande et les ordres à envoyer
- une insérée dans le rover pour le télécommander

Le code utilisé pour les microBit est stocké sur ce dépôt en format Python.

# L'émetteur ou télécommande : microbit 1 (et batterie)

La télécommande envoie des **ondes radios** sur un **canal donné** pour  

Pour faire simple, nous avons choisi **le canal 1**.

Le bouton droit de la télécommande (le bouton A) permet :
- de sélectionner la forme que l'on souhaite effectuer avec le rover
- de l'afficher sur la télécommande
- une fois choisi la forme, de l'envoyer avec le bouton B

Les différents ordres que l'on peut envoyer sont :
- trace un cercle
- trace un carré
- trace un triangle
- fait une danse de la joie

# Le récepteur : microBit 2 and Rover Freenove

La deuxième microbit est simplement enfoncé dans le rover pour lui servir de "cerveau".
Elle reçoit les ordres de la télécommande et les exécute.


# Le support du stylo

...

Bricolé avec des Legos. Il serre l'arrière du rover pour pouvoir tenir un stylo.
C'est assez compliqué en fait, car s'il est trop lourd, le rover n'avance pas ou mal, et si le stylo appuie trop, le rover fait n'importe quoi.
Il faut être délicat et faire des tests.
Tout a très bien fonctionné pour le cercle, par contre le carré et le triangle ne pas prêt pour le support du stylo : le tracé est mauvais.


# Conclusion

En conclusion, la microBit est assez simple à programmer et elle possède beaucoup de capteurs amusants.

Par contre, le robot est beaucoup plus difficile à programmer, et en plus le nôtre a un problème de moteur, l'un est plus faible que l'autre.
Nous avons dû faire en sorte que le moteur droit "compense" la faiblesse de l'autre en avançant plus lentement.

Le fait d'envoyer des informations et des ordres et très amusant et facile. 
Il suffit juste de choisir le même canal des deux cotés et de bien récupérer l'ordre.

Le reste est un peu long à faire (les choix des actions et des ordres, fonction), car nous avons dû beaucoup expérimenter pour trouver des valeurs correctes pour les rotations du rover.

Nous trouvons le résultat un peu décevant par rapport à notre objectif, mais au final, c'était très instructif de voir comment transférer des ordres par ondes radio et d'arriver à faire un télécommande.

Nous n'avons pas trop utilisé de capteurs et fait plus de programmation sur ce projet.

Nous ferons surement d'autres expériences, mais cette fois-ci avec les capteurs qui peuvent se connecter à la microBit.

# Notes

- Nous avons réalisé les programmes avec l'interface "Blocs" qui est plus simple, mais nous avons ensuite utilisé la partie Python pour commenter les programmes.
- Nous avons eu des problèmes pour réaliser le support du stylo et les figures triangle et carré se traçait mal, nous n'avons pas pu les filmer :(
- Le calcul des angles a été compliqué, car il n'existe pas de fonctions pour faire tourner le rover d'un certain angle. Nous avons donc dû répéter et essayer plein de valeurs différentes avant de pouvoir tracer à peu près correctement les figures
- Seul le cercle était assez simple
