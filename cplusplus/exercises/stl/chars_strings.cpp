#include <iostream>
#include <string>
#include <vector>

using namespace std;

void find_something() {
  string sentence = "A quick brown donkey";
  string query = "brown";
  if(sentence.find(query) != string::npos) {
    string::size_type location = sentence.find("brown");
    cout << sentence.substr(location, query.length()) << endl;
  }
}

vector<string> split_string(string s, char delim) {
  vector<string> items;
  auto i = 0;
  auto pos = s.find(delim);
  while (pos != string::npos) {
    items.push_back(s.substr(i, pos-i));
    i = ++pos;
    pos = s.find(delim, pos);
  }
  items.push_back(s.substr(i, s.length()));
  return items;
}

void split_string_delim() {
  string sentence = "A quick brown donkey   ";
  char delim = ' ';
  vector<string> output = split_string(sentence, delim);
  for(const auto &s : output) {
    cout << s << endl;
  }
}

void string_basics() {
  split_string_delim();
}

int main() {
  string_basics();
  return 0;
}
