#include<bits/stdc++.h>
using namespace std;

int main(){

    vector<int> weights = {1, 3, 4, 5};
    vector<int> values = {1, 4, 5, 7};
    int capacity = 7;

    int n = weights.size();
    vector<vector<int>> dp(n + 1, vector<int>(capacity + 1, 0));
    
    for(int i=1; i<=n; ++i){
        for(int j=0; j<=capacity; ++j){

            int cw= weights[i-1];

            if (cw<=j){
                dp[i][j]= max(dp[i-1][j], dp[i-1][j-cw]+values[i-1]);
            }else{
                dp[i][j]= dp[i-1][j];
            }
        }
    }

    cout << dp[n][capacity];

    return 0;
}