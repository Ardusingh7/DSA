#include<bits/stdc++.h>
using namespace std;

int main(){

    vector <int> v= {1,3,5,7};
    int i=0;

    unordered_set <int> seen (v.begin(), v.end());

    while (i<v.size()){

        int x= v[i];
        for(int j=0; j<v.size(); j++){

            if (i==j){
                continue;
            }    
            int d=abs(x-v[j]);
            if (d>0 && seen.find(d)==seen.end()){

                v.push_back(d);
                seen.insert(d);
            }
        }
        i++;
    }

    for(auto x: v){
        cout << x << " ";
    }
    return 0;
}