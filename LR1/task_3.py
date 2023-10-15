list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

half_of_players = len(list_players) // 2

first_team = list_players[:half_of_players]
second_team = list_players[half_of_players:]

print(first_team)
print(second_team)
