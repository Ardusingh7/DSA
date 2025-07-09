#include<bits/stdc++.h>
using namespace std;

int main(){
    
    cout << "Enter string: ";
    string x;
    cin >> x;

    map<char, int> m;

    for(char i:x){
        m[i]++;
    }

    for(auto j:m){

        cout << j.first << "->" << j.second << endl;
    }
    return 0;
} 
