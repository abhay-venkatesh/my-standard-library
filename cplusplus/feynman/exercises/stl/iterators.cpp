#include <iostream>
#include <vector>
#include <iterator>

using namespace std;

int main() {
  vector<int> numbers = { 1, 2, 3, 4, 5 };
  vector<int>::iterator itr = numbers.begin();
  cout << *itr << endl;
  return 0;
}
