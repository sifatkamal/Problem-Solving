#include <bits/stdc++.h>

using namespace std;

int main(){
    
    int a;
    
    cin >> a;
    
    int array_size[a];
    
    double minus_count = 0;
    
    double plus_count = 0;
    
    double zero_count = 0;
    
    for (int i = 0; i < a; i++){
        
        cin >> array_size[i];
        
    }
    
    for (int j = 0; j < a; j++){
        
        if (array_size[j] < 0){
            
            minus_count = minus_count + 1;
            
        }
        
        else if(array_size[j] > 0){
            
            plus_count = plus_count + 1;
            
        }
        
        else{
            
            zero_count = zero_count + 1;
            
        }
        
    }
    
    double b = a;
    
    double result_1;
        
    double result_2;
        
    double result_3;
        
    result_1 = minus_count / b;
        
    result_2 = plus_count / b;
        
    result_3 = zero_count / b;
    
    cout << fixed << setprecision(6) << result_2 << endl;
    
    cout << fixed << setprecision(6) << result_1 << endl;
    
    cout << fixed << setprecision(6) << result_3;
    
    
    return 0;
}
