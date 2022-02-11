import csv
import time

debut = time.time()


def benefice(tab_actions):
    return tab_actions["benefice"]


tableau_actions = []
with open("dataset2_Python+P7.csv", "r") as file:
    reader = csv.reader(file, delimiter=',')
    next(reader)
    for row in reader:
        gain = float(row[2])
        dico = {
            "benefice": gain,
            "Action": row[0],
            "cout": float(row[1])
        }
        tableau_actions.append(dico)

# on trie la liste par benefice afin de slectionner a chaque étape le meilleur benef tant que la contrainte est respecte
tableau_trie = sorted(tableau_actions, key=benefice, reverse=True)

cout_total = 0
meilleur_solution = []
i = 0
while i < len(tableau_actions) and cout_total <= 500:
    action = tableau_trie[i]
    cout_action = action["cout"]
    if cout_total + cout_action <= 500:
        meilleur_solution.append(action["benefice"])
        cout_total = cout_total + cout_action
    i += 1
print(sum(meilleur_solution))
fin = time.time()
print(fin - debut)
