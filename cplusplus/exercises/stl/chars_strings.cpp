#include <iostream>
#include <string>

using namespace std;

void string_basics() {

  // Find something
  string sentence = "A quick brown donkey";
  string query = "brown";
  if(sentence.find(query) != string::npos) {
    string::size_type location = sentence.find("brown");
    cout << sentence.substr(location, query.length()) << endl;
  }

}

int main() {
  string_basics();
  return 0;
}
