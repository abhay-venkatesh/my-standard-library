#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

class Heap {
	vector<int> array;

public:
	Heap() {
		array.push_back(-1);
	}

	void maxHeapify(int i) {
		int max_i = i;
		int li = getLeftChild(i);
		int ri = getRightChild(i);
		if(this->array[li] > this->array[max_i]) {
			max_i = li;
		}
		if(this->array[ri] > this->array[max_i]) {
			max_i = ri;
		}
		if(max_i != i) {
			swap(max_i, i);
			maxHeapify(max_i);
		}
	}

	void swap(int i, int j) {
		int temp = this->array[i];
		this->array[j] = this->array[i];
		this->array[i] = temp;
	}

	/*
	We use 1-indexing (dummy item at 0)

	1----\
	2-\ 3-\
	4 5 6 7 

	If we want to get the parent of 3,
	floor(3/2) = 1

	If we want to get the parent of 6,
	floor(6/2) = 3
	*/
	int getParent(int i) {
		return floor(i/2);
	}

	/*
	1----\
	2-\ 3-\
	4 5 6 7 

	If we want to get the left child of 3,
	2*3 = 6
	*/
	int getLeftChild(int i) {
		return 2*i;
	}

	/*
	1----\
	2-\ 3-\
	4 5 6 7 

	If we want to get the right child of 3,
	(2*3) + 1 = 7
	*/
	int getRightChild(int i) {
		return (2*i) + 1;
	}

	void push(int val) {
		this->array.push_back(this->array.front());
		this->array.front() = val;
		maxHeapify(0);
	}

	int pop() {
		int val = this->array.front();
		this->array.front() = this->array.back();
		this->array.pop_back();
		maxHeapify(0);
		return val;
	}
};

int main() {
	return -1;
}