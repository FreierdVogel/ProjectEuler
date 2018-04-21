from timeit import default_timer as timer
def wait():
	start = timer()
	end = timer()
	while end-start<2:
		end = timer()
		print("Han pasado", end - start, "secs")
	print("Han pasado 2 secs")
wait()