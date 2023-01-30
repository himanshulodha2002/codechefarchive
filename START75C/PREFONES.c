#include <stdio.h>
int max(int x, int y){
    if(x > y){
        return x;
    }else{
        return y;
    }
}

int main(void) {
	// your code goes here
	int t;
	scanf("%d",&t);
	while(t--){
	    int n;
	    scanf("%d",&n);
	    char str[n];
	    scanf("%s",&str);
	    
	    int ans =0;
	    int i=0;
	    for(i=0;i<n;i++){
	        if(str[i] == '1'){
	            ans++;
	        }
	        else{
	            break;
	        }
	    }
	    
	    int sec =0;
	    
	    for(i; i<n;i++){
	        if(str[i]=='1'){
	            int maxone =0;
	            while(str[i++]=='1'){
	                maxone++;
	            }
	            i--;
	            sec=max(sec,maxone);
	            
	        }
	    }
	    printf("%d\n",sec+ans);
	}
	return 0;
}

