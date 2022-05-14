# Projet qr_code

- Le but du programme est de réussir à décoder un QRcode de taille 25 par 25.

## AUTEURS
- Sam BARBOSA
- EThan MACHE

### Fonctionnement du programme

- Le programme est écrit grâce à python 3.

- Le programme utilise la librairie "PIL"  qui permet de charger l'image.

- Pour charger l'image vous devez lancer le programme une fenetre s'ouvre et choississez votre image

- Ensuite,l'image sera vérifier pour détecter les symboles des qrcodes et les lignes en point tillés grâce aux fonctions verify, verify_horizontale() et verify_vertical().

- Si l'image n'est pas le bon sens, c'est-à -dire que les trois carrées ne sont pas en bas à gauche, en haut à gauche et en haut à droite alors la fonction rotate() va faire une rotation jusqu'à obtenir un qrcode dans le bon sens

- Si l'image n'a pas les en point tillés alors le decodage n'est pas possible la fonction verify_horizontale() et verify_vertical()
returnerons "False"

- La fcontion correcteur permet de corriger 4 bits grâce aux bits de corrections.

- Une fois que le Qrcode est dans le bon sens et qu'il y a bien une ligne en point tillés entre chaque symbole. La fonction liste_info() va créer une liste qui sera composée de 14 blocs de 14 bits.


- Une fonction nbr_bloc_decoder()  permet de savoir le nombre de blocs qu'il faudra decoder. La fonction récupère 5 bits aux positions(mat[13][0],mat[14][0],mat[15][0],mat[16][0],mat[17][0]). Ensuite, les 5 bits seront convertis en un nombre en base 10 décimal).


- Maitenant que l'on connaît le nombre de blocs à décoder, on peut décoder le qrcode. La fonction parcourt la liste_bits qui comportent les blocs de 14 bits. Elle prend un bloc par un bloc, la fonction correcteur est appelée pour vérifier s'il y a des erreurs puis les bits sont récupérer et sont converti en nombre en base 10 si à la position mat[24][0] == 0 ou en caractère numérique si [24][0] == 1
La fonction renvoie donc le message codé.













