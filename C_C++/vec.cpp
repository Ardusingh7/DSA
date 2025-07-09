#include <iostream>
#include<vector>
#include<algorithm>
using namespace std;

int main() {

    int n;
    cout << "Enter range: ";
    cin >> n;
    vector <int> v;
    for (int i=0; i<n; i++){
        int x;
        cout << "Enter nums: ";
        cin >> x;
        v.push_back(x);
    }
    for (int i:v){
        cout << i << " ";
    }

    cout << endl;
    sort(v.begin(), v.end(), greater <int>());
    // reverse(v.begin(), v.end());

    for (int i:v){
        cout << i << " ";
    }

    return 0;
}