"""
Two coroutines chained together.

The compute() coroutine is chained to the print_sum() coroutine. The
print_sum() coroutine waits until compute() is completed before it returns a
result.
"""
import asyncio
import random


# Notice the decorator!
@asyncio.coroutine
def compute(x, y):
    print("Compute %s + %s ..." % (x, y))
    # Pause the coroutine for 1 second by yielding from asyncio's built in
    # sleep coroutine. This simulates the time taken by a non-blocking I/O
    # call. During this time the event loop can get on with other things.
    yield from asyncio.sleep(1.0)
    # Actually return a result!
    return x + y


@asyncio.coroutine
def print_sum(x, y):
    # Pause the coroutine until the compute() coroutine has a result.
    result = yield from compute(x, y)
    # The following print() function won't be called until there's a result.
    print("%s + %s = %s" % (x, y, result))


def main():

    # Reference the event loop.
    loop = asyncio.get_event_loop()
    tasks = []

    for i in range(10):
        task = asyncio.ensure_future(print_sum(random.randint(0, 9), random.randint(0, 9)))
        tasks.append(task)


    # Start the event loop and continue until print_sum() is complete.
    loop.run_until_complete(asyncio.wait(tasks))
    # Shut down the event loop.
    loop.close()

if __name__ == "__main__":
    main()

