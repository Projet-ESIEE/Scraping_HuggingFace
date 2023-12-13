from tabulate import tabulate
import json
import random

# Vos résultats de régression ici
regression_results = [
    ["Dep. Variable", "Value"],
    ["R-squared", 0.967],
    ["Adj. R-squared", 0.964],
    # ... Ajoutez les autres résultats de la régression ici
]

# Affichage du tableau dans le terminal
table = tabulate(regression_results, headers="firstrow", tablefmt="tablefmt")
print(table)


def get_user_agent() -> str:
    """
    Read the user_agent.json file and return randomly one
    :return: a user agent | type(str)
    """
    with open('user_agent.json', encoding='utf-8') as agent_list:
        agent_dict = json.load(agent_list)
        random_choice = random.choice(list(agent_dict.keys()))
        return random_choice
