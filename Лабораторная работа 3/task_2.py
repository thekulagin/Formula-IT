# TODO Напишите функцию find_common_participants
def find_common_participants(first_group, second_group, separator = ','):
    first_group_surnames = first_group.split(separator)
    second_group_surnames = second_group.split(separator)
    first_group_surnames = set(first_group_surnames)
    intersections = first_group_surnames.intersection(second_group_surnames)
    intersections = list(intersections)
    intersections.sort()
    return intersections

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group, '|'))