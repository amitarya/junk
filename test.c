#include <stdio.h>

typedef union{
	char b;
	int a;
}A;

A u;
int main(){
	printf("%p %p\n", &u.b, &u.a);
}


