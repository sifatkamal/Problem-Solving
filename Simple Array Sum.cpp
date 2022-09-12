#include <iostream>

using namespace std;

int main(){
    
    int x;
    
    int sum;
    
    int o = 0;
    
    cin >> x;
    
    int myNum[x];
    
    for (int i = 0; i < x; i++){
        
        cin >> myNum[i];
        
        sum = myNum[i] + o;
        
        o = sum;
        
    }
    
    cout << sum;
    
    return 0;
    
}
