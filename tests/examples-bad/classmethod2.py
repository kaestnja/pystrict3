class FooMany(object):
	def __init__(self, a):
		self.a = a
	def foo(self, b):
		self.foovargs(self.a, self.b, 1, 2, 3, 4) ## error: self.b not defined
	def foovargs(self, a, b, *args):
		pass



