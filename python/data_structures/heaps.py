import heapq

class MaxHeapItem:
	def __init__(self, val):
		self.val = val

	def __lt__(self, other):
		return self.val > other.val

class MinHeap:
	def __init__(self):
		self.heap = []

	def push(self, val):
		heapq.heappush(self.heap, val)

	def pop(self):
		return heapq.heappop(self.heap)

	def __len__(self):
		return len(self.heap)

	def __getitem__(self, key):
		return self.heap[key]

class MaxHeap(MinHeap):
	def push(self, val):
		heapq.heappush(self.heap, MaxHeapItem(val))
		
	def pop(self):
		return heapq.heappop(self.heap).val

	def __getitem__(self, key):
		return self.heap[key].val


def main():
	min_heap = MinHeap()
	max_heap = MaxHeap()
	for num in [4, 1, 9, 5, 6]:
		min_heap.push(num)
		max_heap.push(num)

	while min_heap:
		print(min_heap.pop())

	while max_heap:
		print(max_heap.pop())


if __name__ == '__main__':
	main()