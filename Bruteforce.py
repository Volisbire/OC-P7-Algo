import csv
import time

with open("actions_feuille.csv") as actions_feuille:
    reader = csv.DictReader(actions_feuille, quoting=csv.QUOTE_NONNUMERIC)
    tableau_actions = list(reader)

debut = time.time()
nbr_action = len(tableau_actions)
tab_entiers = [i for i in range(2 ** nbr_action)]
# on convertit le tableau des entiers en binaires en retirant les deux premieres caracteres de retour de la fonction bin
tab_binaire = [bin(i)[2:] for i in tab_entiers]
# ajout de 0 pour obtenir des binaires a 20 chiffres
combinaisons = ["0" * (nbr_action - len(k)) + k for k in tab_binaire]
cout_max = 500
combinaisons_possible = []
# on fait la liste de toutes les combinaisons possibles
for combi in combinaisons:
    cout_combinaison = 0
    benefice_combinaison = 0
    for i in range(nbr_action):
        if combi[i] == "1":
            cout_combinaison = cout_combinaison + tableau_actions[i]["cout"]
            benefice_combinaison = benefice_combinaison + tableau_actions[i]["benefice"]
    if cout_combinaison <= cout_max:
        combinaisons_possible.append((combi, benefice_combinaison))
meilleur_investissement = combinaisons_possible[0][0]
benef_max = combinaisons_possible[0][1]
for combi in combinaisons_possible:
    if combi[1] > benef_max:
        benef_max = combi[1]
        meilleur_investissement = combi[0]
liste_meilleur_investissement = []
for i in range(len(meilleur_investissement)):
    if meilleur_investissement[i] == "1":
        liste_meilleur_investissement.append(tableau_actions[i]["Action"])
print(sorted(liste_meilleur_investissement))
fin = time.time()
print(fin - debut)
