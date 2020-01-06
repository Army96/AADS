class Job:
    __slots__ = "_name", "_waitingTime", "_length"

    def __init__(self, name, length):
        self._name = name
        self._waitingTime = 0
        self._length = length

"""
Implements the scheduler. The parameter apq represents an AdaptableHeapPriorityQueue, using the implementation in
the tdp collections folder, the parameter x represent the number of time slices after that the priority of a job has 
to increment
"""
def scheduleJobs(apq, x):
    i = 0
    numSlice = 0            # the number of time slice
    currentJob = None       # the job that cpu is currently processing

    while(True):
        numSlice += 1
        print("Time slice n° ", numSlice)

        # Manages the insertion of new jobs each time slice
        print("Write Y if you want to add a new job, N if you want no new job in this slice: ")
        if(input() == 'Y'):
            name = input("Job name: ")
            length = 0
            priority = -21
            while(length < 1 or length > 100):         # not valid length, reinsert it
                length = int(input("Job length (in time slices): "))
            while(priority < -20 or priority > 19):        # not valid priority, reinsert it
                priority = int(input("Job priority (-20: highest priority, 19: lowest priority): "))
            newJob = Job(name, length)
            if(apq.is_empty() and currentJob == None):
               currentJob = newJob
            else:
                apq.add(priority, newJob)

            print("Job added correctly.")

        # Manages the change of the currently processed job
        if(currentJob is not None):
            i += 1
            if (i > currentJob._length):        # Job completed
                if(not(apq.is_empty())):        # but there aren't elements to process
                    currentJob = apq.remove_min()[1]
                    i = 1
                    print("Job \"" + currentJob._name + "\" in execution...")
                    print("Time slice: ", i, "/", currentJob._length)
                else:
                    currentJob = None
                    print("No jobs in execution now...")
            else:
                print("Job \"" + currentJob._name + "\" in execution...")
                print("Time slice: ", i, "/", currentJob._length)
        else:
            if (not (apq.is_empty())):  # but there aren't elements to process
                currentJob = apq.remove_min()[1]
                i = 1
                print("Job \"" + currentJob._name + "\" in execution...")
                print("Time slice: ", i, "/", currentJob._length)
            else:
                print("No jobs in execution now...")

        print("-------------------------------------------------------------------------------------------------")


        # Manages the update of all the elements of the AdaptablePriorityQueue
        for index in range(len(apq)):
            locator = apq._data[index]
            locator._value._waitingTime += 1
            if(locator._value._waitingTime == x and locator._key != -20):      # the priority increases after x time slices
                locator._key -= 1
                locator._value._waitingTime = 0
            apq.update(locator, locator._key, locator._value)
