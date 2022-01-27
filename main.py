tableau_actions = [{"Action": "Action-1", "cout": 20, "benefice": 1},
                   {"Action": "Action-2", "cout": 30, "benefice": 3},
                   {"Action": "Action-3", "cout": 50, "benefice": 7.5},
                   {"Action": "Action-4", "cout": 70, "benefice": 14},
                   {"Action": "Action-5", "cout": 60, "benefice": 10.2},
                   {"Action": "Action-6", "cout": 80, "benefice": 20},
                   {"Action": "Action-7", "cout": 22, "benefice": 1.54},
                   {"Action": "Action-8", "cout": 26, "benefice": 2.86},
                   {"Action": "Action-9", "cout": 48, "benefice": 6.24},
                   {"Action": "Action-10", "cout": 34, "benefice": 9.18},
                   {"Action": "Action-11", "cout": 42, "benefice": 7.14},
                   {"Action": "Action-12", "cout": 110, "benefice": 9.9},
                   {"Action": "Action-13", "cout": 38, "benefice": 8.74},
                   {"Action": "Action-14", "cout": 14, "benefice": 0.14},
                   {"Action": "Action-15", "cout": 18, "benefice": 0.54},
                   {"Action": "Action-16", "cout": 8, "benefice": 0.64},
                   {"Action": "Action-17", "cout": 4, "benefice": 0.48},
                   {"Action": "Action-18", "cout": 10, "benefice": 1.4},
                   {"Action": "Action-19", "cout": 24, "benefice": 5.04},
                   {"Action": "Action-20", "cout": 114, "benefice": 20.52},
                   ]
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
        combinaisons_possible.append((combi, cout_combinaison))
print(combinaisons_possible)
