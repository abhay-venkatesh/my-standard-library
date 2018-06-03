/*

Find 3 numbers such that their sum is the closest possible to the
target number.

For example,
v = < 1, -2, 4, -3 >
target =  0
output = < -2, 4, -3 >
sum = -1

Approach 1: Brute force
Try all possible combinations, O(factorial)

Approach 2: Dynamic programming
Start with sub-problem of size 3
Then, for problem of size 4, take the 3 numbers that produce
min(dist(target, sum)) by trying all three

Approach 3:

*/

#include <iostream>
#include <vector>

using namespace std;

vector<int> three_sum_closest(vector<int> v, int target) {

}

int main() {
  return 0;
}
