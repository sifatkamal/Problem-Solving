#include <iostream>

using namespace std;

int main(){
    
    int num_1[3];
    
    int num_2[3];
    
    int A = 0;
    
    int B = 0;
    
    for (int i= 0; i < 3; i++){
        
        cin >> num_1[i];
    
    }
    
    for (int i= 0; i < 3; i++){
        
        cin >> num_2[i];
    
    }
        
    for (int j = 0; j < 3; j++){    
        
        if (num_1[j] > num_2[j]){
            
            A++;
            
        }
        
        else if (num_1[j] < num_2[j]){
            
            B++;
            
        }
        
        
    }
    
    cout << A << " ";
    
    cout << B;
    
    return 0;
    
}
