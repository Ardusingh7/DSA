#include<iostream>
#include<algorithm>
#include<vector>
#include<numeric>

using namespace std;

int main(){

    int n, x;
    vector <int> v;

    cout << "Enter range: ";
    cin >> n;
    
    for(int i=0; i<n; i++){

        int x;
        cin >> x;
        v.push_back(x);
    }

    cout << "Enter num to count: ";
    cin >> x;
    cout << "Min element: ";
    cout << *min_element(v.begin(), v.end());
    cout << endl;
    cout << "Max element: ";
    cout << *max_element(v.begin(), v.end());
    cout << endl;
    cout << "Reversed list: ";
    reverse(v.begin(), v.end());

    for(int i:v){
        cout << i << " ";
    }
    
    cout << endl;
    cout << "Count is: ";
    cout << count(v.begin(), v.end(), x);
    cout << endl;
    cout << "Sum is: " << accumulate(v.begin(), v.end(), 0);

    return 0;
}