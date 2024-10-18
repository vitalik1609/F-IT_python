# TODO Напишите функцию find_common_participants

def find_common_participants(group1, group2, sep=','):
        return list(set(group1.split(sep)).intersection(set(group2.split(sep))))


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой

print(find_common_participants(participants_first_group, participants_second_group, '|'))
