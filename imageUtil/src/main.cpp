#include <fstream>
#include <iostream>
#include <tlvObjects.h>
#include <pixMap.h>


using namespace std;

int main(int argc, char *argv[]) {
	if (argc < 3) {
		cout << "Usage: ./imageConverter <input binary image> <output file>"
			  << endl;
		exit(1);
	}
	fstream ifile;
	fstream ofile;
	ifile.open(argv[1], ios::in|ios::binary|ios::ate);
	ofile.open(argv[2], ios::out);

	if (ifile.is_open() && ofile.is_open()) {
		size_t size = ifile.tellg();
		ifile.seekg(0, ios::beg);
		byte_t *input = new byte_t[size];
		ImageInterpreter image;
		size_t begin = 0;
		ifile.read((char *)input, size);

		if (!image.Interpret(input, begin, size - 1)) {
			cout << "ERROR: Image Binary doesn't seem to be correct\n";
			exit(1);
		}
		vector<unique_ptr<TLVObject>> &objs = image.GetSubObjects();
		PixMap::Init();
		string outputStr;
	 	for (int i = 0; i < objs.size() ; i++) {
			objs[i]->DumpPixMap();
#ifdef DEBUG
			objs[i]->Dump();
#endif
		}

		PixMap::GetInstance()->Dump(outputStr);
		if (!outputStr.empty()) {
			ofile.write(outputStr.c_str(), outputStr.size());
		}
		delete[] input;
	} else {
		cout << "ERROR: Can't open input binary or output file\n";
	}
	return 0;
}
