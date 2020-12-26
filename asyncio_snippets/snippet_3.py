import asyncio
import time


async def hello():
    print("Hello, ", end="")
    await asyncio.sleep(1)
    print("world!")


async def say_after(delay, msg):
	await asyncio.sleep(delay)
	print(msg)


async def main():
	await say_after(1, "Hello")
	await say_after(2, "World")

if __name__ == "__main__":
	start = time.time()

	asyncio.run(main())

	end = time.time()
	print(f"Took {end-start} seconds.")