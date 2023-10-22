salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
capital = 0

while months:
    months -= 1
    if months == 9:
        capital = spend - salary
    else:
        spend += spend * increase
        capital += spend - salary
        
months = 10
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(capital, 2))
