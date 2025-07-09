#include<bits/stdc++.h>
using namespace std;

int main(){

    vector <int> array={8, 7, 6, 1, 0, 9, 2};
    int high= array.size()-1;
    int low=0;

    int pivot = array[high];
  
    // pointer for greater element
    int i = (low - 1);

    // traverse each element of the array
    // compare them with the pivot
    for (int j = low; j < high; j++) {
        if (array[j] <= pivot) {
            
        // if element smaller than pivot is found
        // swap it with the greater element pointed by i
        i++;
        
        // swap element at i with element at j
        swap(array[i], array[j]);
        }
    }
    swap(array[i + 1], array[high]);
    for(auto x: array){
        cout << x << " ";
    }
    cout << "\n";
    cout << i+1;

        return 0;
    }