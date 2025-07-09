#include <iostream>
#include <vector>
#include <climits>
using namespace std;

int kadane(vector<int>& nums) {
    int maxSoFar = INT_MIN;
    int maxEndingHere = 0;

    for (int i = 0; i < nums.size(); i++) {
        maxEndingHere += nums[i];
        maxSoFar = max(maxSoFar, maxEndingHere);

        // if the current sum drops below 0, reset
        if (maxEndingHere < 0) {
            maxEndingHere = 0;
        }
    }

    return maxSoFar;
}

int main() {
    vector<int> arr = {1,2,-3,4,-4,5,-4,3};
    cout << "Max subarray sum: " << kadane(arr) << endl;
    return 0;
}
