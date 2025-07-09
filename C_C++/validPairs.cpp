#include <bits/stdc++.h>
using namespace std;

int countGoodSubarrays(vector<int>& nums, int k) {
    unordered_map<int, int> freq; // to store frequency of elements
    int pairCount = 0;      // current number of equal pairs
    int left = 0;                 // left pointer of the window
    int ans = 0;            // total good subarrays

    for (int right = 0; right < nums.size(); ++right) {
        // Before adding nums[right], how many nums[right] do we have?
        cout << "Adding " << nums[right] << ": already seen " << freq[nums[right]] << " times" << endl;
        
        // Each existing occurrence of nums[right] will make one pair
        pairCount += freq[nums[right]];
        freq[nums[right]]++;

        cout << "PairCount after adding: " << pairCount << endl;

        // Shrink the window from the left if we already have enough pairs
        while (pairCount >= k) {
            ans += nums.size() - right; // all subarrays [left...right], [left+1...right]... are good
            cout << "  --> Subarray [" << left << "..." << right << "] is good. Adding " << (nums.size() - right) << " to ans" << endl;

            // Remove nums[left] from the window
            pairCount -= freq[nums[left]] - 1;
            freq[nums[left]]--;
            cout << "  --> Shrinking window, removing " << nums[left] << ", new pairCount: " << pairCount << endl;
            left++;
        }
        cout << "=====\n";
    }

    return ans;
}

int main() {
    int n, k;
    cout << "Enter size of array: ";
    cin >> n;
    vector<int> nums(n);
    cout << "Enter array elements:\n";
    for (int i = 0; i < n; i++) cin >> nums[i];
    cout << "Enter k: ";
    cin >> k;

    int res = countGoodSubarrays(nums, k);
    cout << "Total good subarrays: " << res << endl;
    return 0;
}
