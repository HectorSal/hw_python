def func_counter(func):
	def wrapper(input):
		wrapper.counter = wrapper.counter + 1
		return func(input)
	wrapper.counter = 0
	return wrapper
