#include <iostream>
#include <vector>

using namespace std;

int main(){
    // read first line for sizes
    int n;
    int q;
    cin >> n >> q;
    // read second line for reefs
    vector<int> query;
    for (int i = 0; i < n; i++){
        int next;
        cin >> next;
        query.push_back(next);
    }
    // read following lines for queries
    vector<int> ans;
    for(int i = 0; i < q; i++){
        int a, b;
        cin >> a >> b;
        int x = query[a-1];
        for(int j = a; j < b; j++){
            x = x ^ query[j];
        }
        cout << x << endl;
    }

    return 0;
}

/*
prefix sum array algorithm
*/