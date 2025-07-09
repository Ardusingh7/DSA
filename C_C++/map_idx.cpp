#include <iostream>
#include <map>
#include <vector>
using namespace std;

int main() {
    vector<int> v = {5, 3, 5, 2, 3, 1};
    map<int, vector<int>> indexMap;

    for (int i = 0; i < v.size(); i++) {
        indexMap[v[i]].push_back(i);
    }

    for (auto p : indexMap) {
        cout << p.first << "->";
        for (int idx : p.second)
            cout << idx << " ";
        cout << endl;
    }

    return 0;
}
