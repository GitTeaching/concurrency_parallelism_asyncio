import concurrent.futures
import time

def do_something(seconds):
	print(f'Sleeping for {seconds} second(s)')
	time.sleep(seconds)
	return f'Done Sleeping for {seconds} second(s)...'


if __name__ == "__main__":
	start = time.time()

	params = [5, 4, 3, 2, 1]

	with concurrent.futures.ProcessPoolExecutor() as executor:
		results = executor.map(do_something, params)

		for result in results:
			print(result)


	end = time.time()

	print(f'Finished in {end-start} second(s)')