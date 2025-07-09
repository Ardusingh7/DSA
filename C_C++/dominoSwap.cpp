#include<bits/stdc++.h>
using namespace std;

int main(){

    // tops = [2,1,2,4,2,2], bottoms = [5,2,6,2,3,2]

    vector<int> top= {2,1,2,4,2,2};
    vector<int> down= {5,2,6,2,3,2};

    unordered_map<int, int> topf;
    unordered_map<int, int> downf;
    int maxFt=0;
    int maxFd=0;

    for(int i=0; i<top.size(); i++){

        topf[top[i]]++;
        downf[down[i]]++;
        maxFt= max(maxFt, topf[top[i]]);
        maxFd= max(maxFd, downf[down[i]]);
    }

    if(maxFt>maxFd){
        
        int maxEle;

        for(auto x: topf){
            if(x.second==maxFt){
                maxEle=x.first;
            }
        cout << maxEle;
        }
    }else{
        cout << maxFd;
    }

    return 0;
}