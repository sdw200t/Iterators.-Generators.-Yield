# 1.Написать итератор, который принимает список списков, и возвращает их плоское представление, 
# т.е последовательность состоящую из вложенных элементов. 
class FlatIterator:

	cur = 0
	lst = []

	def __init__(self, lst):
		self.lst = self.flat_list(lst)

	def flat_list(self, lst, res = []):
		for item in lst:
			if isinstance(item, list):
				self.flat_list(item, res)
			else:
				res.append(item)
		return res

	def __iter__(self):
		return self

	def __next__(self):
		if self.cur < len(self.lst):
			res = self.lst[self.cur]
			self.cur += 1
			return res
		else:
			raise StopIteration
		
nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, [3, 4, [5, 6]]],
]

for item in FlatIterator(nested_list):
	print(item)   

#flat_list = [item for item in FlatIterator(nested_list)]
#print(flat_list)


