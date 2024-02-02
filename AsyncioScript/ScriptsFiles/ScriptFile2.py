import time
import asyncio

print("{:*^50}".format("I am from script2 - start"))


async def run_method():
    count = 0
    while True:
        if count < 10:
            await asyncio.sleep(1)
            count += 1
            print(f"Sleep from 'II', Count: {count} ")
        else:
            break
    return True


async def main():
    task1 = asyncio.create_task(run_method())
    await task1


if __name__ == '__main__':
    asyncio.run(main())
    print("{:*^50}".format("I am from script2 - end"))
