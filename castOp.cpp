#include <iostream>

using namespace std;

class A{
	private:
		int a;

	public:
		operator int (){
			return a;
		}
		void operator=(int &i){
			a = i;
		}
};

template <typename T>
class B{
	private:
		T a;

	public:
		operator int (){
			return a;
		}
		void operator=(T &i){
			a = i;
		}

};

void far(B<int> b) {
	int y = b;
	cout << y << endl;
}

int main() {
	A a;
	B<int> b;
	int x = a;
	int y = b;

	cout << x << " " << y << endl;
	far(a);
	cout << x << " " << y << endl;

}
