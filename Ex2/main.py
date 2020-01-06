from TdP_collections.priority_queue.adaptable_heap_priority_queue import AdaptableHeapPriorityQueue
from Ex2.CPUScheduler import scheduleJobs
from Ex2.CPUScheduler import Job

apq = AdaptableHeapPriorityQueue()

# riempio la coda con alcuni job per provare il funzionamento dello scheduler in queste altre condizioni
job1 = Job("job1", 3)
job2 = Job("job2", 5)
job3 = Job("job3", 20)

apq.add(10, job1)
apq.add(-5, job2)
apq.add(-15, job3)

scheduleJobs(apq, 10)