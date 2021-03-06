from collections import deque

class Solution:
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        
        [A: 3, B: 3], n = 2
         ^     
         A
        
        We need to find an optimal scheduling algorithm.
        I think round-robin could potentially be optimal. 
        What if n = 0? It is still optimal, we just never have to be idle.
        
        We want to find the least number of CPU intervals required. 
        In order to do so, we basically minimize the idle time. We can minimize idle time by 
        scheduling tasks of different types back to back. 
        
        [B: 0, C: 1], n = 0
        A, B, C, B, C, _, 
        
        By sorting, we ensure that counting from the most frequently
        occuring task makes sense, or we'd have to maintain an n for 
        each task. So each task would have a cooldown but that seems like a 
        lot of work to maintain.
        
        [A: 0, B: 0, C: 0], n = 3
        A, B, C, _, A
        
        --- A different model ---
        Can we improve our algorithm using a different data structure? 
        Perhaps a queue? It seems natural to use queues in scheduling 
        problems. 

        It helps with mutating the list and simplifying our code.
        We pull a task out of the buffer, decrement it, 
        and then put it back. Perhaps we create another buffer,
        and then once we done with our cooldown, we can replace
        the buffer with the new buffer, and start again, till the list is out.
        """
        tasks_with_counts = self.getTasksWithCounts(tasks)
        tasks_with_counts.sort(reverse=True)
        n_ = n + 1

        """
        intervals = 0
        buffer = [(3, 'A'), (2, 'B'), (1, 'C')]
        buffer_ = []
        n_ = 3


        """
        intervals = 0
        buffer = deque(tasks_with_counts)
        buffer_ = deque()
        while buffer:
            while buffer or n_ > 0:
                if not buffer and not buffer_:
                    return intervals 
                if buffer:
                    task = buffer.popleft()
                    num = task[0]
                    name = task[1]
                    num -= 1
                    if num > 0:
                        buffer_.append((num, name))
                n_ -= 1
                intervals += 1
            buffer = buffer_
            buffer_ = deque()
            n_ = n + 1
            
        return intervals
        
    def getTasksWithCounts(self, tasks):
        count = 0
        prev = None
        tasks_with_counts = []
        for task in tasks:
            if not prev:
                prev = task
                count = 1
            else:
                if task == prev:
                    count += 1
                else:
                    tasks_with_counts.append((count, prev))
                    prev = task
                    count =  1
        if prev:
            tasks_with_counts.append((count, prev))

        return tasks_with_counts

"""
--- A Failing Test ---
Input = ["A","A","A","A","A","A","B","C","D","E","F","G"]
2

We need to update our scheduling algorithm. The issue is that we need
to spread out the Task A. In our scheduling pipeline, we should put in the
task with the most counts, but we should also pull it out as soon as the 
cooldown has finished. 

buffer = [(A, 6), (B, 1), (C, 1), (D, 1), (E, 1), (F, 1), (G, 1)]

Priority queue? With priority as the cooldown time left.
But then how do we handle time? At every point in our algorithm,
we are at a different piece of time.

--- A new algorithm --

buffer = [(A, 6), (B, 1), (C, 1), (D, 1), (E, 1), (F, 1), (G, 1)]

optimal scheduling: 
A, B, C, A, D, E, A, F, G, A, _, _, A, _, _, A

How did I do it? Well, for this particular algorithm, I knew I had to
spread out A over the course of the execution in order to maximize its usage.

If know what an optimal scheduling looks like, then we can try and find 
out how to write a procedure that takes items out of our buffer, and then
schedules them. 

I need to find a way to be able to pull A out, when needed,

--- Track ending time instead ---
We maintain two buffers now, one contains all the jobs that need to be done,
and then the other is the queue, which the scheduler places stuff onto.

--- Track earliest possible time ---
jobs = [A, A, A, A, B, C, D], n = 2
queue = [(A, 0), (A, 3), (A, 6), (A, 9), (B, 0), (C, 0), (D, 0)]

We basically place into the queue the earliest possible time the
task could be scheduled. 

We make this queue a priority queue, and then we pull out stuff from the queue
according to the earliest time it could be scheduled. 
It is important to order first by priority, and then by letter. 

But this is incorrect. It will schedule A, B, C, D... which is wrong.

--- Number of tasks, and then earliest possible time ---


"""
    
def main():
    pass

if __name__ == "__main__":
    main()