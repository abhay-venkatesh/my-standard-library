#include <iostream>

using namespace std;

/*

   The idea is to use a carriage container,
   and then update this carriage container accordingly,
   to keep adding the right binary digit to the return string.

   c \in {0,1,2,3}
   (c % 2) \in {0,1}
   (c \ 2) \in {0,1}

*/
string add_binary(string a, string b) {
  string s = "";
  int c = 0, i = a.size() - 1, j = b.size() - 1;
  while(i >= 0 || j >= 0 || c == 1) {
    c += i >= 0 ? a[i--] - '0' : 0;
    c += j >= 0 ? b[j--] - '0' : 0;
    s = char(c % 2 + '0') + s;
    c /= 2;
  }
  return s;
}

int main() {
  return 0;
}
