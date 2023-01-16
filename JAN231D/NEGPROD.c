#include <stdio.h>

int main(void) {
	// your code goes here
	int t,i,a,b,c;
	
	scanf("%d",&t);
	for(i=1;i<=t;i++){
	    //fflush(stdin);
		scanf("%d%d%d",&a,&b,&c);
	    //printf("%d%d%d\n",a,b,c);
		((a*b)<0 || (b*c)<0 || (c*a)<0)
			?printf("YES\n")
			:printf("NO\n");
	}
	return 0;
}

