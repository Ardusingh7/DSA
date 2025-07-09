#include <iostream>
#include <map>
#include <vector>
using namespace std;

int main() {
    vector<string> words = {"apple", "banana", "apricot", "blueberry", "avocado"};
    map<char, vector<string>> groups;

    for (string word : words) {
        groups[word[0]].push_back(word);
    }

    for (auto pair : groups) {
        cout << pair.first << ": ";
        for (string s : pair.second) {
            cout << s << " ";
        }
        cout << endl;
    }

    return 0;
}
