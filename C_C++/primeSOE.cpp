#include<bits/stdc++.h>
using namespace std;

int main(){

    cout << "Enter n: ";
    int n;
    cin >> n;

    vector <bool> primes(n+1, true);
    primes[0] = primes[1] = false;

    /*for(auto x: primes){
        cout << x << " ";
    }*/

    int p=2;

    while (p*p<=n){

        if(primes[p]){
            for(int i=p*p; i<=n; i+=p){
                primes[i]=false;
            }
        }
        p++;
    }

    for(int i=0; i<=n; i++){
        if (primes[i]){
            cout << i << " ";
        }
    }

    return 0;
}