#include <bits/stdc++.h>

using namespace std;

int main(){
    
    unsigned long long int arrayy[5];
    
    for (int i = 0; i < 5; i++){
        
        cin >> arrayy[i];
        
    }
    
    //MAX
    
    unsigned long long int max = arrayy[0];
    
    for (int j = 0; j < 5; j++){
        
        if (max < arrayy[j] ){
            
            max = arrayy[j];
            
        }
        
    }
    
    //MIN
    
    unsigned long long int min = arrayy[0];
    
    for (int k = 0; k < 5; k++){
        
        if (min > arrayy[k]){
            
            min = arrayy[k];
            
        }
        
    }
    
    
    //MAX SUM
    
    unsigned long long int max_sum = 0;
    
    unsigned long long int sum_1 = 0;
    
    for (int l = 0; l < 5; l++){
        
        if (arrayy[l] == max){
            
            continue;
            
        }
        
        else{
            
            sum_1 = arrayy[l] + max_sum;
            
            max_sum = sum_1;
            
        }
        
    }    
        
    //MIN SUM
    
    unsigned long long int min_sum;
    
    min_sum = 0;
    
    unsigned long long int sum_2 = 0;
        
    for (int l = 0; l < 5; l++){
        
        if (arrayy[l] == min){
            
            continue;
            
        }
        
        else{
            
            sum_2 = arrayy[l] + min_sum;
            
            min_sum = sum_2;
            
        }
        
        
    }
    
    if (max_sum == 0){
        
        if (min_sum == 0){
            
            max_sum = arrayy[0] * 4;
            
            min_sum = arrayy[0] * 4;
            
        }
        
    }
        
    
    cout << max_sum << " ";
    
    cout << min_sum;
    
    return 0;
    
}
