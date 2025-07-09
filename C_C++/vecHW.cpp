#include<iostream>
#include<vector>
#include<set>
#include<algorithm>
using namespace std;

int main(){

    int n;
    cout << "Enter range: ";
    cin >> n;

    vector<int> v;

    for(int i=0; i<n; i++){

        int x;
        cin >> x;
        v.push_back(x);
    }

    for(int x:v){
        cout << x << " ";
    }
    
    // sort(v.begin(), v.end());

    set<int> s(v.begin(), v.end());

    cout << endl;

    for(int x:s){
        cout << x << " ";
    }
    return 0;
}