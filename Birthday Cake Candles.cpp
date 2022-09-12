#include <bits/stdc++.h>

using namespace std;

int main(){
    
    unsigned long long int n;
    
    cin >> n;
    
    unsigned long long int arrayy[n];
    
    for (int i = 0; i < n; i++){
        
        cin >> arrayy[i];
        
    }
    
    //MAX
    
    unsigned long long int max = arrayy[0];
    
    for (int j = 0; j < n; j++){
        
        if (max < arrayy[j] ){
            
            max = arrayy[j];
            
        }
        
    }
    
    unsigned long long int count = 0;    
        
    for (int k = 0; k < n; k++){
        
        if (arrayy[k] == max){
            
            count = count + 1;
            
        }
        
    }
    
    cout << count;
    
    return 0;
    
}
