import pulp as plp


def main():
    problem = plp.LpProblem("CompanyProduction", plp.LpMaximize)

    x1 = plp.LpVariable("x1", lowBound=0, cat=plp.LpInteger)  # Lemonade
    x2 = plp.LpVariable("x2", lowBound=0, cat=plp.LpInteger)  # Fruit juice

    problem += x1 + x2, "AmountOfProducts"  # Objective function

    problem += 2 * x1 + x2 <= 100, "Water"  # Water constraint
    problem += x1 <= 50, "Sugar"  # Sugar constraint
    problem += x1 <= 30, "LemonJuice"  # Lemon juice constraint
    problem += x2 <= 40, "FruitJuice"  # Fruit juice constraint
    problem += 2 * x2 <= 40, "FruitPuree"  # Fruit puree constraint

    problem.solve(solver=plp.PULP_CBC_CMD(msg=False))

    print("Status:", plp.LpStatus[problem.status])
    for v in problem.variables():
        print(v.name, "=", v.varValue)

    print("Maximum amount of products:", plp.value(problem.objective))


if __name__ == "__main__":
    main()
