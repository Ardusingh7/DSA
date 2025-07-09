#include <bits/stdc++.h>
using namespace std;

int main() {
    vector<int> arr = {1, 3, 4, 5};
    int k = 5;
    int n = arr.size();

    // dp[i][j] = true if we can make sum j using first i items
    vector<vector<bool>> dp(n + 1, vector<bool>(k + 1, false));

    // Base case: sum 0 is always possible (by taking nothing)
    for (int i = 0; i <= n; i++)
        dp[i][0] = true;

    for (int i = 1; i <= n; i++) {  
        for (int j = 0; j <= k; j++) {
            int curr = arr[i - 1];
            if (curr <= j) {
                dp[i][j] = dp[i - 1][j] || dp[i - 1][j - curr];
            } else {
                dp[i][j] = dp[i - 1][j];
            }
        }
    }

    cout << "Subset sum " << k << " possible: " << (dp[n][k] ? "Yes" : "No") << endl;
    return 0;
}
