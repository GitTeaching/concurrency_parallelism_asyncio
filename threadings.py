# Threading - Pre-emptive Multitasking
# The operating system decides when to switch tasks external to Python
# One processor running at the same time
# Used to speed up I/O Bound programs

# Thread implementation using concurent.futures module and manually (threading odule)
import concurrent.futures
import threading
import time


def do_something(seconds):
	print('Sleeping...')
	time.sleep(seconds)
	return f'Done sleeping {seconds} second(s)..'


if __name__ == '__main__':
	start = time.time()

	#create threads manually using threading module
	threads = []
	for _ in range(5):
	    t = threading.Thread(target=do_something, args=[1])
	    t.start()
	    threads.append(t)
	for thread in threads:
	    thread.join()

	#create one thread th1 and print returned result
	with concurrent.futures.ThreadPoolExecutor() as executor:
		th1 = executor.submit(do_something, 1)
		print(th1.result())

	#create multiple threads using a list comprehension and print returned resuts in order of completion
	with concurrent.futures.ThreadPoolExecutor() as executor:
		results = [executor.submit(do_something, 1) for _ in range(5)]
	for result in concurrent.futures.as_completed(results): 
		print(result.result())

	#create multiple threads with diffrent param for each thread
	params = [5, 4, 3, 2, 1]
	with concurrent.futures.ThreadPoolExecutor() as executor:
		results = [executor.submit(do_something, param) for param in params]
	for result in concurrent.futures.as_completed(results): 
		print(result.result())

	#create multiple threads using map method
	params = [5, 4, 3, 2, 1]
	with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
		#results = [executor.submit(do_something, 1) for _ in params]
		results = executor.map(do_something, params)
	for result in results:
		print(result)

	end = time.time()

	print(f'Finished in {end-start} second(s)')