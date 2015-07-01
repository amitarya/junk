#include <memory>
#include <iostream>

using namespace std;
class A {
	public:
	string a;
	shared_ptr<int> sptr;
	bool flag;
	bool flag2;
	bool flag3;
	virtual void foo(){}
};
A b;
int main(){
	b.a = "This is a test string";
	cout << sizeof(b)<< endl;
}
