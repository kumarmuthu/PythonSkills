# Python progress bar(tqdm)
***
## **Steps to go:**

1. Create the progress bar based on the user-given runtime
2. The 'main()' function to create two threads,
* 2.1 Thread one is for 'create_progress_bar' function, update the tqdm(progress bar) total percentage and customize the progress bar colour.
* 2.2 Thread second one is for the 'calculate_elapse_time' function, this function will calculate every second until the end time,
 this function will control/decide the progress bar end time.
3. Function 'display_progress_bar' will display the progress bar based on the calculated x% percentage.

if we comment it out the line:53, the progress bar will keep updating the progress percentage in one line
***

**Example:**

User given time: 30sec

Calculated percentage(%): 27

Display percentage(%): 3 [last 3% only show on console]

end...
***

**Execution video available on Youtube:** https://youtu.be/cN9YlmNcTRc

**Email:-** kumarmuthuece5@gmail.com

***
