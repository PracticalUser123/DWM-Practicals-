# Import the required library
from apyori import apriori

# Creating sample transactions
transactions = [
    ['Milk', 'Bread', 'Saffron'],
    ['Milk', 'Saffron'],
    ['Bread', 'Saffron', 'Wafer'],
    ['Bread', 'Wafer']
]

# Generating association rules
rules = list(apriori(transactions, min_support=0.5, min_confidence=0.5))

# Extracting rules from the object
for i in range(len(rules)):
    for rule in rules[i][2]:
        LHS = list(rule[0])
        RHS = list(rule[1])
        support = rules[i][1]
        confidence = rule[2]
        lift = rule[3]
        print("LHS:", LHS, "--", "RHS:", RHS)
        print("Support:", support)
        print("Confidence:", confidence)
        print("Lift:", lift)
        print(10 * "----")
