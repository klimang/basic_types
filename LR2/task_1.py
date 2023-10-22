money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

months = 0
while money_capital > 0:
    months += 1
    if months:
        spend += increase * spend
        money_capital += salary - spend
    else:
        money_capital += salary - spend

print("Количество месяцев, которое можно протянуть без долгов:", months)
