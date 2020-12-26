import asyncio


async def task(num: int):
    print(f"Task {num}: request sent")
    await asyncio.sleep(1)
    print(f"Task {num}: response arrived") 


async def main():
	# 1 - concurrently
	await asyncio.gather(*[task(x) for x in range(1,4)])

	print("-"*20)

	# 2 - non concurrently
	for i in range(1, 4):
		await task(i)

	print("-"*20)

	# 3 - concurrently
	# create_task schedules coroutines to run soon concurrently
	task1 = asyncio.create_task(task(1))
	task2 = asyncio.create_task(task(2))
	task3 = asyncio.create_task(task(3))
	await task1
	await task2
	await task3

	print("-"*20)

	# 4 - concurrently
	# ensure_future schedules coroutines to run soon concurrently (Python < 3.7)
	task1 = asyncio.ensure_future(task(1))
	task2 = asyncio.ensure_future(task(2))
	task3 = asyncio.ensure_future(task(3))
	await task1
	await task2
	await task3

	print("-"*20)

	# 5 - concurrently
	try:
		await asyncio.wait_for(task(1), timeout=0.5)
	except asyncio.TimeoutError:
		print("timeout!")


if __name__ == '__main__':
	# runs coroutine main
    asyncio.run(main())
