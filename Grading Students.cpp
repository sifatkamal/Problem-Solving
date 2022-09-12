#include <bits/stdc++.h>

using namespace std;

int main(){
    
    int a;
    
    int n;
    
    cin >> n;
    
    for (int i = 0; i < n; i++){
        
        cin >> a;
        
        if (a < 38){
            
            cout << a << endl;
            
        }
        
        else if (a >= 38){
            
            int multi_1;
            
            int multi;
            
            multi_1 = a / 5;
            
            multi = (multi_1 + 1) * 5;
            
            if (multi - a == 2){
                
                cout << multi << endl;
                
            }
            
            else if (multi - a == 1){
                
                cout << multi << endl;
                
            }
            
            else{
                
                cout << a << endl;
                
            }
            
        }
        
    }    
    
    return 0;

}
