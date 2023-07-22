#include <bits/stdc++.h>
using namespace std;
#define ll long long


int main() {


    int a;
    cin>>a;
    if(a==0){
        cout << "No";
        exit(0);
    }
        
    //std::cout << std::fixed << std::setprecision(6) << a/b << std::endl;
    if(a%2 ==0 && a > 2){
        cout << "YES";
    }
    else{
        cout << "NO";
    } 
    return 0;
}
