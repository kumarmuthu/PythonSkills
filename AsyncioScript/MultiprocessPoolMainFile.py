import os
import multiprocessing
import subprocess
import asyncio


def run_script(script_path, terminate_event=None, condition=None):
    try:
        subprocess.run(["python", script_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running {script_path}: {e}")


def another_fc(m_str, count=None):
    print(f"I am from another func: {m_str}, {count}")


def run_task(task, args):
    task(*args)


async def main():
    # Get the current script's directory
    current_script_dir = os.path.dirname(os.path.abspath(__file__))

    # Replace 'script1.py' and 'script2.py' with the actual names of your scripts
    script_names = ['ScriptsFiles/ScriptFile1.py', 'ScriptsFiles/ScriptFile2.py']

    # Create a pool of processes
    with multiprocessing.Pool(processes=len(script_names) + 1) as pool:
        # Map each script to a separate process with relative path
        # script_paths = [os.path.join(current_script_dir, script_name) for script_name in script_names]
        # # Map the script execution function to each script
        # pool.map(run_script, script_paths)
        # pool.apply_async(another_fc)

        # Map each script and function to a separate process with relative path
        script_paths = [os.path.join(current_script_dir, script_name) for script_name in script_names]
        tasks = [(run_script, [script_path]) for script_path in script_paths]
        tasks.append((another_fc, ('muthu', 10)))
        # tasks.pop(0)
        # tasks.pop(0)
        # Map the tasks to each process
        # pool.starmap(lambda task, args: task(*args), tasks)
        pool.starmap(run_task, tasks)

        # Optionally, wait for all processes to finish
        pool.close()
        pool.join()


if __name__ == '__main__':
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(main())
    # loop.close()
    asyncio.run(main())

    '''
    simple example:
    # import asyncio
    import time
    
    async def coroutine_one():
        print("Coroutine One: Start")
        await asyncio.sleep(5)
        print("Coroutine One: End")
    
    async def coroutine_two():
        print("Coroutine Two: Start")
        await asyncio.sleep(1)
        print("Coroutine Two: End")
    
    async def main():
        task1 = asyncio.create_task(coroutine_one())
        task2 = asyncio.create_task(coroutine_two())
    
        await task1
        await task2
    '''
