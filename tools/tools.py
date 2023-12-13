from tabulate import tabulate

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
