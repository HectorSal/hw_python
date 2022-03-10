def func_counter(func):
	def wrapper():
		wrapper.counter = wrapper.counter + 1
		return func()
	wrapper.counter = 0
	return wrapper
