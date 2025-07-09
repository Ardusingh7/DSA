#include<bits/stdc++.h>
using namespace std;

int main(){

    cout << "Enter range: ";
    int n;
    cin >> n;

    vector <int> v;
    vector <int> v2;

    for(int i=0; i<n; i++){

        cout << "Enter nums: ";
        int x;
        cin >> x;
        v.push_back(x);
    }

    sort(v.begin(), v.end());

    int i=0;
    int j=n-1;

    while (i<j){

        v2.push_back(v[j]);
        v2.push_back(v[i]);

        j--;
        i++;
    }

    for(auto x: v2){

        cout << x << " ";
    }

    return 0;

}