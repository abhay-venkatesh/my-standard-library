#include <iostream>

using namespace std;

/*

We simply search the number line for the square root.

--- my_sqrt(x = 5) ---
1 2 3 4 5
left = 2, right = 2, mid = 2

*/
int my_sqrt(int x) {
  int left = 1, right = x;
  while (left <= right) {
    int mid = (left + right)/2;
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
