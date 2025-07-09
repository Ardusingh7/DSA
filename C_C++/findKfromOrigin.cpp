#include <bits/stdc++.h>
using namespace std;

int partition(vector<int> &v, int l, int h) {
    int pivot = v[h];
    int i = l - 1;

    for (int j = l; j < h; j++) {
        if (v[j] < pivot) {
            i++;
            swap(v[i], v[j]);
        }
    }
    swap(v[i + 1], v[h]);
    return i + 1;
}

int quickSelect(vector<int> &v, int l, int h, int k) {
    if (l <= h) {
        int p = partition(v, l, h);

        if (p == k) return v[p];
        else if (k < p) return quickSelect(v, l, p - 1, k);
        else return quickSelect(v, p + 1, h, k);
    }
    return -1; // if k is out of range
}

int main() {
    vector<int> v = {8, 1, 2, 5, 4, 2, 3, 7};
    int k = 5; // looking for the 6th smallest element (0-based index)

    if (k >= 0 && k < v.size()) {
        int result = quickSelect(v, 0, v.size() - 1, k);
        cout << "The " << k + 1 << "-th smallest element is: " << result << endl;
    } else {
        cout << "k is out of range" << endl;
    }

    return 0;
}
