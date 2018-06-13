#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int op_increase(int i) { return ++i; }

void transform_into_from(vector<int> source, vector<int> dest) {
  cout << "Source: ";
  for(const auto &n : source) {
    cout << n << " ";
  }
  cout << endl;
  cout << "Dest: ";
  transform(source.begin(), source.end(), dest.begin(), op_increase);
  for(const auto &n : dest) {
    cout << n << " ";
  }
  cout << endl;
}

void transform_demo() {
  vector<int> source = {1,2,3,4,5};
  vector<int> dest;
  dest.resize(source.size());
  transform_into_from(source, dest);
}

int main() {
  transform_demo();
  return 0;
}
