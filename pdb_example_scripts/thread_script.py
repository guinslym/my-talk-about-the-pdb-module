# python 2.7
# https://github.com/Kozea/wdb
from threading import Thread 

def work(x):
	print(x)
	import wdb; wdb.set_trace()

for i in range(3):
	Thread(
		target=work, args(1,)
		).start()