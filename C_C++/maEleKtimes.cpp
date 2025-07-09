#include<bits/stdc++.h>
using namespace std;

int main(){

    // nums = [1,3,2,3,3], k = 2

    vector <int> v= {1,3,2,3,3};
    int k=2;
    int x= *max_element(v.begin(), v.end());

    int ans=0;
    int l=0;

    for(int r=0; r<v.size(); r++){

        if (v[r]==x){
            k--;
        }
        while (k<=0){
            ans+=v.size()-r;

            if(v[l]==x){
                k++;
            }
            l++;
        }
    }
    cout << ans;
    return 0;
}