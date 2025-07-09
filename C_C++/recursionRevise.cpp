#include<bits/stdc++.h>
using namespace std;

void printNums(int x){
    
    if(x==1) 
    cout << 1 << " ";
    else{
        
        cout << x << " ";
        printNums(x-1);
    } 
}

int main(){

    printNums(5);
    return 0;
}