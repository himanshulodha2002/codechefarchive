#include <iostream>
using namespace std;

int main() 
{
	int t;
	cin>>t;
	while(t--)
	{
	    int n;
	    cin>>n;
	    string a,b;
	    cin>>a>>b;
	
	    int o=0;int m=0;
	    for(int i=0;i<n;i++)
	    {
	        o+= (a[i]=='0');
            m+= (b[i]=='0');
        }
	    if (o==m)cout<<"yes"<<endl;
	    else cout<<"no"<<endl;
    }
	return 0;
}
