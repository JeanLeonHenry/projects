import std/random
import std/strutils

const END = "»"
const tirade = """Agressif : « Moi, monsieur, si j’avais un tel nez,
Il faudrait sur-le-champ que je me l’amputasse ! »
Amical : « Mais il doit tremper dans votre tasse !
Pour boire, faites-vous fabriquer un hanap ! »
Descriptif : « C’est un roc !… c’est un pic !… c’est un cap !
Que dis-je, c’est un cap ?… C’est une péninsule ! »
Curieux : « De quoi sert cette oblongue capsule ?
D’écritoire, monsieur, ou de boîte à ciseaux ? »
Gracieux : « Aimez-vous à ce point les oiseaux
Que paternellement vous vous préoccupâtes
De tendre ce perchoir à leurs petites pattes ? »
Truculent : « Çà, monsieur, lorsque vous pétunez,
La vapeur du tabac vous sort-elle du nez
Sans qu’un voisin ne crie au feu de cheminée ? »
Prévenant : « Gardez-vous, votre tête entraînée
Par ce poids, de tomber en avant sur le sol ! »
Tendre : « Faites-lui faire un petit parasol
De peur que sa couleur au soleil ne se fane ! »
Pédant : « L’animal seul, monsieur, qu’Aristophane
Appelle Hippocampelephantocamélos
Dut avoir sous le front tant de chair sur tant d’os ! »
Cavalier : « Quoi, l’ami, ce croc est à la mode ?
Pour pendre son chapeau, c’est vraiment très commode ! »
Emphatique : « Aucun vent ne peut, nez magistral,
T’enrhumer tout entier, excepté le mistral ! »
Dramatique : « C’est la Mer Rouge quand il saigne ! »
Admiratif : « Pour un parfumeur, quelle enseigne ! »
Lyrique : « Est-ce une conque, êtes-vous un triton ? »
Naïf : « Ce monument, quand le visite-t-on ? »
Respectueux : « Souffrez, monsieur, qu’on vous salue,
C’est là ce qui s’appelle avoir pignon sur rue ! »
Campagnard : « Hé, ardé ! C’est-y un nez ? Nanain !
C’est queuqu’navet géant ou ben queuqu’melon nain ! »
Militaire : « Pointez contre cavalerie ! »
Pratique : « Voulez-vous le mettre en loterie ?
Assurément, monsieur, ce sera le gros lot ! »""".split(END)[0 ..< ^1]

randomize()
echo sample(tirade).strip() & " " & END