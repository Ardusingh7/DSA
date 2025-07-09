#include<bits/stdc++.h>
using namespace std;

int main(){

    vector<int> v= {-1,-4,-1,4};
    
    int sum3=0; 

    for(int i=0; i<3; i++){
        sum3+=v[i];
    }
    int r=2;
    int l=0;
    int cnt=0;

    while(r<v.size()){

        int midEle= (r+l)/2;
        
        if(2*(sum3-v[midEle])==v[midEle]){
            cnt++;
        }

        r++;
        // cout << sum3 << " ";
        sum3+= v[r]-v[l];
        l++;
    }

    // cout << endl;
    cout << cnt; 

    return 0;
}