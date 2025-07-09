#include <bits/stdc++.h>
using namespace std;

int main() {
    vector<int> v = {1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0};
    int l = 0;
    int k = 4;
    int ans = 0;

    for (int r = 0; r < v.size(); r++) {
        if (v[r] == 0) {
            k--;
        }

        while (k < 0) {
            if (v[l] == 0) {
                k++;
            }
            l++;
        }
        ans = max(ans, r - l + 1);
    }
    cout << ans;    
    return 0;
}
