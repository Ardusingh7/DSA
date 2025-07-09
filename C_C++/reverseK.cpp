#include<bits/stdc++.h>
using namespace std;

int main(){

    vector <int> v={1,2,3,4,5,6,7,8};
    int k=3; // if k is ZERO; return v
    
    int n= v.size();
    for(int i=0; i<n; i+=k){
        int j=i+k;

        j=min(j, n);
        reverse(v.begin()+i, v.begin()+j);
    }

    for(auto x: v){
        cout << x << " ";
    }

    return 0;
}