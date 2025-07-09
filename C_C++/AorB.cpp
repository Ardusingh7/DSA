#include <bits/stdc++.h>
using namespace std;

int main() {
    vector<int> v = {1, 1, 1, 0, 1, 1};
    map<int, vector<int>> m;

    int cnt1 = 0, cnt0 = 0;

    for (int i = 0; i < v.size(); i++) {
        m[v[i]].push_back(i);
    }

    for (auto x : m) {
        vector<int> vec = x.second;
        int cnt = 1; 
        int last = vec[0];

        for (int i = 1; i < vec.size(); i++) {
            if (vec[i] > last + 1) {
                cnt++;
                last = vec[i];
            }
        }

        if (x.first == 0)
            cnt0 = cnt;
        else
            cnt1 = cnt;
    }

    if (cnt0 >= cnt1)
        cout << 0;
    else
        cout << 1;

    return 0;
}
