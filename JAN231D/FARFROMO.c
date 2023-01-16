#include <stdio.h>
#include<math.h>

int main(void) {
	// your code goes here
	int t,i,x1,y1,x2,y2;
	double a,b;
	
	scanf("%d",&t);
	for(i=1;i<=t;i++){
	    //fflush(stdin);
	    scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
	    //printf("%d%d%d%d\n",a,b,c,d);
	    //((a*b)<0 || (b*c)<0 || (c*a)<0)?printf("YES\n"):printf("NO\n");
	    
	    a=sqrt(x1*x1+y1*y1);
	    b=sqrt(x2*x2+y2*y2);
	    if(a==b)
	        printf("EQUAL\n");
	    else if(a>b)
	        printf("ALEX\n");
	    else if(a<b)
	        printf("BOB\n");
	}
	return 0;
}

