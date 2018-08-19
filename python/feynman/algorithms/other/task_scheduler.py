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
            buffer = []
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
                    tasks_with_counts.append((count, task))
                    prev = task
                    count =  1
        if prev:
            tasks_with_counts.append((count, prev))

        return tasks_with_counts
    
def main():
    s = Solution()
    tasks = ["A", "A", "A", "B", "B", "C"]
    print(s.leastInterval(tasks, 3))

if __name__ == "__main__":
    main()