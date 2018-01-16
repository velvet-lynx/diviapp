class DictList:

	def __init__(self, datas=None):
		if not datas:
			datas = []
		self.datas = datas

	def set_datas(self, datas):
		self.datas = datas

	def get_datas(self):
		return self.datas

	def add(self, data):
		if type(data) is dict:
			self.datas.append(data)

	def replace(self, index, dic):
		self.datas[index] = dic

	def to_sub_dict(self, data, keys=None):
		if not keys:
			return self.datas
		else:
			return {key:data[key] for key in keys if key in data}

	def to_tuples_set(self, keys=None):
		result = set()
		for data in self.datas:
			temp = ()
			for value in self.to_sub_dict(data, keys).values():
				temp += (value,)
			result.add(temp)
		return result

	def to_sub_list(self, keys=None):
		return [self.to_sub_dict(data, keys) for data in self.datas]

	def is_empty(self):
		return not self.datas

	def __repr__(self):
		return str(self.datas)
