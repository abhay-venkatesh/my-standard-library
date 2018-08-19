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
        
        [A: 3, B: 3, C: 2], n = 5
        """
        
    def tasksWithCounts(self, tasks):
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
                    tasks_with_counts.append((prev, count))
                    prev = task
                    count =  1
        if prev:
            tasks_with_counts.append((prev, count))

        return tasks_with_counts
    
def main():
    pass

if __name__ == "__main__":
    main()