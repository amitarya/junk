#include <iostream>
#include <cstddef>

using namespace std;
#pragma pack(push, 1)
struct Bit
{
	    unsigned char a_:1;
};
#pragma pack(pop)
typedef struct Bit bit;

class A{
private:
	bit a[1];
public:
	void SetM1(int i);
	bool GetM1(int &);
   int m1;
};

bool A::GetM1(int &i){
	int b = *((int *) &a);
	if (b&1 == 1) {
		i = m1;
		return true;
	} else {
		return false;
	}
}

void A::SetM1(int i) {
	m1 = i;
	int *b = (int *)a;
	*b |= 1;
}

int main(){
	A a;
	cout << sizeof(A) <<" "<<offsetof(A, m1) <<" "<< sizeof(bit) << endl;
	int i = 5;
	cout << a.GetM1(i) << endl;
	cout << i << endl;
	a.SetM1(6);
	cout << a.GetM1(i) << endl;
	cout << i << endl;
}
