#include <iostream>
#include <string>
#include <cmath>

using std::cout;
using std::endl;
using std::cin;
using std::string;
using std::power;

/* rules:
 A += 1
 B += 2
 AB += 4 and not individual values
*/

int main(){
    int n;
    cin >> n;
    string s;
    cin >> s;
    int score = 0;
    int abCount = 0;

    for(int i = 0; i < n; i++){
        char c = s[i];
        if(c == 'A'){
            if(i < n-1 && s[i+1] == 'B'){
                score += 4;
                abCount++;
                i++;
            } else {
                score++;
            }
        } else if(c == 'B'){
            score++;
        }
        else if(c == 'C'){
            score -= (abCount * abCount);
        }
    }
    cout << score << endl;
}