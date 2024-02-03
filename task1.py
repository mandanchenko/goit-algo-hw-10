import pulp as plp

prob = plp.LpProblem("Напої", plp.LpMaximize)

x1 = plp.LpVariable("x1", 0, None, cat=plp.LpContinuous)
x2 = plp.LpVariable("x2", 0, None, cat=plp.LpContinuous)

prob += x1 + x2, "Profit"

prob += 2 * x1 + 1 * x2 <= 100, "Вода"
prob += 1 * x1 <= 50, "Цукор"
prob += 1 * x1 <= 30, "Лимонний сік"
prob += 2 * x2 <= 40, "Фруктове пюре"

prob.solve()
print(f"Status: {plp.LpStatus[prob.status]}")
print(f"Лимонад = {plp.value(x1)}")  # x1.varValue
print(f"Фруктовий сік = {plp.value(x2)}")
print(f"Максимальна кількість напоїв = {plp.value(prob.objective)}")
