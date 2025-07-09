#include<bits/stdc++.h>
using namespace std;

int main(){

    // piles = [3,6,7,11], h = 8

    vector <int> piles= {3,6,7,11};
    sort(piles.begin(), piles.end());
    int h=8;
    int cnt=0;
    int maxEle= *max_element(piles.begin(), piles.end());
    map <int, int> ans;

    for(int i=1; i<=maxEle; i++){
        for(int j=0; j<piles.size(); j++){

            cnt+=ceil((double)piles[j]/(double)i);
        }
    ans[i]+=cnt;
    cnt=0;
    }

    for(auto x: ans){
        
        cout << x.first << ":" << x.second << "\n";
    }

    cout << endl;

    int maxMin= INT_MAX;

    for(auto x: ans){
        if(x.second<=h){
            maxMin= min(maxMin, x.first);
        }
    }
    cout << maxMin;
    return 0;
}