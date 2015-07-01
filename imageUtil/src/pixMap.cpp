#include <interpreter.h>
#include <pixMap.h>
#include <iomanip>
#include <sstream>

using namespace std;
unique_ptr<PixMap> PixMap::_instance;

void
PixMap::Init() 
{
	_instance = unique_ptr<PixMap>(new PixMap());
}

PixMap*
PixMap::GetInstance() {
	return _instance.get();
}

string&
PixMap::GetFilename() {
	return _filename;
}

void
PixMap::SetFilename(char *name, size_t length) {
	char *end = name + length;
	while (name < end) {
		_filename.append(1, name[0]);
		name++;
	}
}


void
PixMap::AddRow()
{
	_numRows++;
	_rgbRowList.push_back(vector<RGB>(0));
}


void
PixMap::AddRGBList(byte_t red, byte_t green, byte_t blue) {
	RGB rgbrow = {red, green, blue};
	_rgbRowList[_numRows - 1].push_back(rgbrow);
}


void
PixMap::AddKey(byte_t key, byte_t red, byte_t green, byte_t blue)
{
	RGB rgb = {red, green, blue};
	_keyPixelMap[key] = rgb;
}

void
PixMap::Dump(string& outputString)
{
	stringstream ss;
	if (!VerifyAndFixRowSize()) {
		cout << "[PixMap::Dump] PixRows don't match in size\n" << endl;
		return;
	}
	ss << _filename << "\n";
	ss << _rowSize << " ";
	ss << _numRows << "\n";
	for (int i = 0; i < _rgbRowList.size(); i++) {
		ss << "\n";
		for (int j = 0; j < _rgbRowList[i].size(); j++ ) {
			ss << setfill('0') << setw(2) << hex << (size_t)
				_rgbRowList[i][j]._red << " ";
			ss << setfill('0') << setw(2) << hex << (size_t)
				_rgbRowList[i][j]._green << " ";
			if (j != _rgbRowList[i].size() - 1) {
				ss << setfill('0') << setw(2) << hex << (size_t)
					_rgbRowList[i][j]._blue << " ";
			} else {
				ss << setfill('0') << setw(2) << hex << (size_t)
					_rgbRowList[i][j]._blue;
			}
		}
	}
	ss << "\n\n";
	outputString = ss.str();
}


bool
PixMap::VerifyAndFixRowSize() {
	int rowSize = 0;
	for (int i = 0; i < _rgbRowList.size(); i++) {
		if (rowSize != 0 && rowSize != _rgbRowList[i].size()) {
			return false;
		}
		if (rowSize == 0) {
			rowSize = _rgbRowList[i].size();
		}
	}
	_rowSize = rowSize;
	return true;
}

