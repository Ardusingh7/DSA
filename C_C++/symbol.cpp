#include<bits/stdc++.h>
using namespace std;

int main(){

    int n=5;
    vector <char> shirts;
    vector <char> pants;

    for(int i=0; i<n; i++){
        char x;
        cout << "Enter element: ";
        cin >> x;
        shirts.push_back(x);
    }

    for(int i=0; i<n; i++){
        char x;
        cout << "Enter element: ";
        cin >> x;
        pants.push_back(x);
    }

    sort(shirts.begin(), shirts.end());

    for(auto x: shirts){
        cout << x << " ";
    }

    return 0;
}