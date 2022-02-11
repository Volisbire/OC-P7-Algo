import csv
import math
import time

debut = time.time()


def benefice(actions_tab):
    return actions_tab["benefice"]


tableau_actions = []
with open("dataset2_Python+P7.csv", "r") as file:
    reader = csv.reader(file, delimiter=',')
    next(reader)

    for row in reader:
        gain = float(row[2])
        cout = float(row[1])
        dico = {
            "benefice": gain / cout if cout > 0 else math.inf,
            "Action": row[0],
            "cout": cout,
            "gain": gain
        }
        tableau_actions.append(dico)

sorted_tab = sorted(tableau_actions, key=benefice, reverse=True)

cout_total = 0
meilleur_solution = []
i = 0
while i < len(tableau_actions) and cout_total <= 500:
    action = sorted_tab[i]
    cout_action = action["cout"]
    if cout_total + cout_action <= 500 and action["benefice"] != math.inf:
        meilleur_solution.append(action["Action"])
        cout_total = cout_total + cout_action
    i += 1
print(meilleur_solution)
fin = time.time()
print(fin - debut)
