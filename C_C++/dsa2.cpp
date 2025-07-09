#include<bits/stdc++.h>
using namespace std;

int main(){

    cout << "Enter range: ";

    int n;
    cin >> n;

    vector <int> v;

    for(int i=0; i<n; i++){

        cout << "Enter nums: ";
        int x;
        cin >> x;
        v.push_back(x);
    }

    int s1= accumulate(v.begin(), v.end(),0);
    int s2= ((n+1)*(n+2))/2;

    cout << s1 << " " << s2;

    cout << s2-s1 << endl;

    return 0;
}