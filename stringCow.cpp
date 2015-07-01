#include<iostream>
#include <cstdlib>

using namespace std;

int main() {
	string s1;
	cin >> s1;
	string s2 = s1;
	cout << (void *)s2.c_str() << endl;
	cout << (void *)s1.c_str() << endl;
	s1.replace(0,1, "P");
	s2.replace(0,1, "N");
	cout << (void *)s2.c_str() << endl;
	cout << (void *)s1.c_str() << endl;

}
