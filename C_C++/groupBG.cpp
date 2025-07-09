#include<bits/stdc++.h>
using namespace std;

int main() {
    vector<int> v = {1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0};
    int l = 0;

    // TOTAL NUMS OF BOYS THAT CAN BE GROUPED TOGETHER

    int cnt1 = 0;
    for (auto x : v) {
        if (x == 1) {
            cnt1++;
        }
    }

    int mink = 0;

    // START WITH NUMS OF GIRLS IN 1st WINDOW

    for (int i = 0; i < cnt1; i++) {
        if (v[i] == 0) {
            mink++;
        }
    }

    // FIND THE WINDOW WITH THE MIN CNT
    
    int ans = mink;
    int r = cnt1;

    while (r < v.size()) {
        if (v[l] == 0) mink--;
        if (v[r] == 0) mink++;
        l++;
        r++;
        // cout << l << ":" << r << ":" << mink << "\n";
        ans=min(ans, mink);
        // ans = min(ans, mink); // If you want minimum
    }

    cout << ans << endl;

    return 0;
}
