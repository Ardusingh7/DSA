#include<bits/stdc++.h>
using namespace std;

int main(){

    cout << "Enter range: ";
    int n;
    cin >> n;

    vector <int> v;
    unordered_map <int, int> m;
    for(int i=0; i<n; i++){

        cout << "Enter nums: ";
        int x;
        cin >> x;
        v.push_back(x);
    }

    for(auto x: v){

        m[x]++;
    }

    for(auto x: m){
        if(x.second>n/2){
            cout << x.first;
            return 0;
        }
    }
    cout << -1 << endl;

    return 0;
}