#include<bits/stdc++.h>
using namespace std;

int main(){

    vector <int> v= {2, 7, 9, 3, 1};
    int n= v.size();

    vector <int> chori(n,0);
    chori[0]=v[0];
    chori[1]=max(v[0], v[1]);

    cout << chori[0] << " " << chori[1] << " ";
    for(int i=2; i<n; i++){
        chori[i]=max(chori[i-1], v[i]+chori[i-2]);
        cout<< chori[i] << " ";
    }

    cout << chori[n-1];
    return 0;
}