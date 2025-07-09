#include<bits/stdc++.h>
using namespace std;

/*The value of a triplet of indices (i, j, k) is equal to (nums[i] - nums[j]) * nums[k].
Example 1:
Input: nums = [12,6,1,2,7]
Output: 77*/

int main(){

    vector <int> nums= {12,6,1,2,7};
    int n= nums.size();
    vector <int> maxL (n);
    vector <int> maxR (n);
    
    maxL[0]= nums[0];
    maxR[n - 1] = nums[n - 1];
    
    for(int i=1; i<n; i++){
        maxL[i]=max(maxL[i-1], nums[i]);
    }

    for (int i = n - 2; i >= 0; i--) {
        maxR[i] = max(maxR[i + 1], nums[i]);
    }

    int maxTriple=0;

    for(int j=1; j<n; j++){
        maxTriple= max(maxTriple, (maxL[j-1]-nums[j])*maxR[j+1]);
    }

    cout << maxTriple;
    return 0;
}