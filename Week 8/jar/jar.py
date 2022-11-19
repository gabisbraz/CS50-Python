class Jar:
	def __init__(self, capacity=12):
		if capacity < 0:
			raise ValueError("Capacidade Errada")
		self._capacity = capacity
		self._size = 0

	def __str__(self):
		return self.size * '🍪'

	def deposit(self, n):
		if n > self.capacity:
			raise ValueError("Muitos cookies!")
		if self.size + n > self.capacity:
			raise ValueError("Muitos cookies!")
		self._size += n

	def withdraw(self, n):
		if n > self._size:
			raise ValueError("Retirada de cookies maisor do que o valor de cookies!")
		self._size -= n

	@property
	def capacity(self):
		return self._capacity

	@property
	def size(self):
		return self._size

jar = Jar()
jar.deposit(5)
jar.withdraw(0)
print(jar)