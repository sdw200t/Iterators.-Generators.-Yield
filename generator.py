from iterator import FlatIterator

# 2.Написать генератор, который принимает список списков, и возвращает их плоское представление. Например
# Должен отпечататься каждый элемент каждого вложенного списка
def flat_generator(nested_list):
	flat_list = [item for item in FlatIterator(nested_list)]
	cnt = 0
	while cnt < len(flat_list):
		yield flat_list[cnt]
		cnt += 1

nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, [3, 4, [5, 6]]],
]

for item in flat_generator(nested_list):
	print(item)