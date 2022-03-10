import time

def calculate_time(func):
	def wrapper():
		start = time.time()
		func()
		end = time.time()
		elapsed_time = end - start
		print(f"Total time {elapsed_time}")
	return wrapper
