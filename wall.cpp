#include <iostream>
#include <vector>

using namespace std;

int main(){
    int n;
    cin >> n;
    vector<int> wall;
    for(int i = 0; i < n; i++){
        int next;
        cin >> next;
        wall.push_back(next);
    }

    for(int i = 0; i < n; i++){
        // find max diff from i-2 to i
        int max = 0;
        for(int j = i-2; j < i; j++){
            if(j < 0){
                continue;
            }
            int diff = abs(wall[i] - wall[j]);
            if(diff > max){
                max = diff;
            }
        }
        // if max is greater than 4 print false
        if(max > 4){
            cout << "False" << endl;
            return 0;
        }
        // find max diff from i to i+2
        max = 0;
        for(int j = i; j < i+2; j++){
            if(j >= n){
                continue;
            }
            int diff = abs(wall[j] - wall[i]);
            if(diff > max){
                max = diff;
            }
        }
        // if max is greater than 4 print false
        if(max > 4){
            cout << "False" << endl;
            return 0;
        }
    }
    cout << "True" << endl;
    return 0;
}