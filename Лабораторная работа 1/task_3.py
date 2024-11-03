list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

players_amount = len(list_players)
players_in_team = players_amount // 2

first_team = list_players[:players_in_team]
second_team = list_players[players_in_team:]

print(first_team)
print(second_team)
