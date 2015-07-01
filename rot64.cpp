#include <iostream>
#include <string.h>
#include <fstream>

using namespace std;

void
Encrypt(unsigned char *str, int length)
{
	for (int i=0;i<length;i++) {
		//cout << str[i] << " ";
		str[i]=(str[i]+64)%128;
		//cout << "-->" << str[i] << endl;
	}
}

int
main(int argc, char * argv[])
{
	if (argc < 2) {
		cout << "Usage : ./a.out  filename";
	}
	ifstream fin;
	ofstream fout;
	fin.open(argv[1]);
	fout.open("output.txt");
	while(true) {
		if (fin.eof()) {
			break;
		}
		string str;
		fin >> str;
		unsigned char *str_copy = new unsigned char[str.size()];
		memcpy(str_copy, str.c_str(), str.size());
		Encrypt(str_copy, str.size());
		fout << str_copy << endl;
		delete str_copy;
	}
}
