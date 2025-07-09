#include<bits/stdc++.h>
using namespace std;

int main(){

    vector<int> v = {5, 6, 1, 2, 3, 2, 4, 5, 1, 6};
    map<int, int> m;

    for(int x:v){

        m[x]++;
    }

    for(auto p:m){

        cout << p.first << " ";
        }
    return 0;
}