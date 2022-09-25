import asyncio
import time

async def foo(text):
    print(text)
    await asyncio.sleep(1)
    print(f"{text}_finished")


async def woo(text):
    print(text)
    await asyncio.sleep(5)
    print(f"{text}_finished")

async def main():
    start = time.time.now()
    # await foo("hey")
    task = asyncio.create_task(woo("long_time")) # run this task without waiting
    await task # wait until it`s finished(block)
    print(time.time.now()-start)
    task = asyncio.create_task(foo("text")) # run this task without waiting
    await task # wait until it`s finished
    print(time.time.now()-start)

    # we want the finished to be run except for waiting for the sleep code
    print("finished")

asyncio.run(main())



