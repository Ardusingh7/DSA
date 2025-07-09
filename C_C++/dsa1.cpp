#include<bits/stdc++.h>
using namespace std;

int main(){

    cout << "Enter range: ";
    int n, k;
    cin >> n;
    cout << "Enter K: ";
    cin >> k;

    vector <int> v;

    for(int i=0; i<n; i++){

        cout << "Enter nums: ";
        int x;
        cin >> x;
        v.push_back(x);
    }

    set <int> seen;

    for(int i=0; i<v.size(); i++){

        int y= k-v[i];
        
        if (seen.find(y) != seen.end()) {
            
            cout << "YES";
            return 0;
        }
        else{
            seen.insert(v[i]);
        }
    }

    cout << "NO" << endl;

    return 0;
}