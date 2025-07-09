#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<vector<int>> matrix = {
        {1, 3, 1, 2},
        {1, 5, 1, 3},
        {4, 2, 1, 7}
    };

    int rows = matrix.size();
    int cols = matrix[0].size();

    for (int d = 0; d < rows + cols - 1; d++) {
        for (int i = 0; i <= d; i++) {
            int j = d - i;
            if (i < rows && j < cols) {
                cout << matrix[j][i] << " ";
            }
        }
    }

    return 0;
}
