CPUScheduler.py
CPUScheduler contain the Job class used in the algorithm and the scheduleJobs(AdaptableHeapPriorityQueue, int) function.
The scheduleJobs required in input an AdaptableHeapPriorityQueue of Job (this Queue can be empty) and an integer that
represent the number of time slice that a job must wait for increment his priority.
The output is represent by the various prints during the run of this function (because the infinite loop never end).
The class Job contain three parameter (_name, _waitingTime and _length), but the __init__ method requires only two
of this, _name (type string) and _length (type int).

main.py
In this class we test the CPUScheduler.
To test the CPUScheduler we need to import the classes related to the AdaptableHeapPriorityQueue and to the Job class
and the scheduleJobs function, through the following lines of code:
from TdP_collections.priority_queue.adaptable_heap_priority_queue import AdaptableHeapPriorityQueue
from Ex2.CPUScheduler import scheduleJobs
from Ex2.CPUScheduler import Job