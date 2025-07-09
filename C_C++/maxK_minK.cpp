#include<bits/stdc++.h>
using namespace std;

int main() {

    vector<int> v = {1,2,3,4,5,1,2,6,5};
    int minK = 2;
    int maxK = 5;
    
    long long cnt = 0;
    int l = -1; // last bad index (where v[i] not in range)
    int minPos = -1, maxPos = -1; // last position of minK and maxK

    for (int i = 0; i < v.size(); i++) {
        if (v[i] < minK || v[i] > maxK) {
            l = i; // bad element encountered
        }
        if (v[i] == minK) minPos = i;
        if (v[i] == maxK) maxPos = i;

        int validStart = min(minPos, maxPos);
        if (validStart > l) {
            cnt += (validStart - l);
        }
    }

    cout << cnt << endl;

    return 0;
}
