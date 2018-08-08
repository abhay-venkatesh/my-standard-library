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

Approach 2: Sort the array
Have three different counters

----------------------
 ^
^                    ^

Now, these three will produce a sum somewhere near the target number.

-3 -1 1 4 7 8 10
 ^
    ^         ^

target = 5
curr_sum = 6

We want to decrease current sum. Therefore, we can only move the counter
on 10.

-3 -1 1 4 7 8 10
 ^
    ^       ^

target = 5
curr_sum = 4

Now, we want to increase the value, therefore,

-3 -1 1 4 7 8 10
 ^
      ^
              ^

target = 5
curr_sum = 6

Proof goal: we want to show that we have tried all combinations needed
to get to the right solution.

*/

#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

vector<int> three_sum_closest(vector<int> v, int target) {
  if(v.size() == 3) return v;

  sort(v, v.size());

  int closest_sum = v[0] + v[1] + v[v.size()-1];
  for(int i = 0; i < v.size()-2; i++) {
    int j = i + 1;
    int k = v.size()-1;
    while(j < k) {

      int curr_sum = v[i] + v[j] + v[k];

      if(curr_su)

      if(curr_sum == target)
        return vector<int>{v[i],v[j],v[k]};
      else if(curr_sum < target) j++;
      else k--;


    }
  }


}

int main() {
  return 0;
}
