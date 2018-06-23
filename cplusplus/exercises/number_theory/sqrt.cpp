#include <iostream>

using namespace std;

/*
x = 5
left = 1
right = 2
mid = 1

*/
int my_sqrt(int x) {
  int left = 1, right = x;
  while (left <= right) {
    int mid = left + (right - left)/2;
    if (mid == x/mid) {
      return mid;
    } else if (mid < x/mid) {
      left = mid + 1;
    } else {
      right = mid - 1;
    }
  }
  return right;
}

int main() {
  return 0;
}
