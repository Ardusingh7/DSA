#include<bits/stdc++.h>
using namespace std;

int main(){

    cout << "Enter range: ";
    int n, k;
    cin >> n;
    cout << "Enter K: ";
    cin >> k;

    vector <int> v;
    map<int, int> m;

    for(int i=0; i<n; i++){

        cout << "Enter nums: ";
        int x;
        cin >> x;
        v.push_back(x);
    }

    for(int i=0; i<n; i++){
   
        int x= k-v[i];
        if(m.find(x)!=m.end())
        {
            cout << m[x] << " " << i;
            break;
        }else
        {
        m[v[i]]=i;
        }
    }

    return 0;
}