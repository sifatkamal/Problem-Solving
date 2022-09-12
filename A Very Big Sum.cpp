#include <iostream>

using namespace std;

int main(){
    
    int x;
    
    long long int sum;
    
    long long int o = 0;
    
    cin >> x;
    
    long long int myNum[x];
    
    for (long long int i = 0; i < x; i++){
        
        cin >> myNum[i];
        
        sum = myNum[i] + o;
        
        o = sum;
        
    }
    
    cout << sum;
    
    return 0;
    
}
