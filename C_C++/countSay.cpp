#include<bits/stdc++.h>
using namespace std;

/*int main(){
    
    // using brute  force

    vector <int> v= {1,7,9,2,5};

    int l=11;
    int u=11;

    int cnt=0;

    set <int> seen;
    seen.insert(v[0]);

    for(int i=1; i<v.size(); i++){

        for(auto x: seen){
            if((v[i]+x)>=l && (v[i]+x)<=u){
                cnt++;
            }
        }
        seen.insert(v[i]);
    }

    cout << cnt;
    return 0;
}*/

#include <bits/stdc++.h>
using namespace std;

int main() {
    vector<string> seen;
    seen.push_back("1");

    for (int i = 1; i < 5; i++) {
        string x = seen.back(); // fixed here!
        int cnt = 1;
        string naya = "";

        for (int j = 1; j < x.size(); j++) {
            if (x[j] == x[j - 1]) {
                cnt++;
            } else {
                naya += to_string(cnt) + x[j - 1];
                cnt = 1;
            }
        }
        naya += to_string(cnt) + x.back(); // don't forget last group
        seen.push_back(naya);
    }

    for (auto x : seen) {
        cout << x  << "\n"; 
    }

    return 0;
}
