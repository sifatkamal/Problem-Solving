#include <iostream>

using namespace std;

int main(){
    
    int n;
    
    cin >> n;
    
    int m;
    
    m = n;
    
    int lol = 0;
    
    //column
    
    for (int i = 0; i < n; i++){
        
        //row
        
        for (int j = 0; j < n + 1; j++){
            
            if (lol == m){
            
                cout << "#";
                
            }
            
            else{
                
                if (j==0){
                    
                    lol = lol + 1;
                    
                    continue;
                    
                }
                
                else{
                
                    cout << " ";
                
                    lol = lol + 1;
                
                }
                
            }
            
        }
        
        m = m - 1;
            
        lol = 0;
                
        cout << endl;
        
    }
    
    return 0;
    
}

