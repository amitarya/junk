#ifndef PIXMAP_H
#define PIXMAP_H

#include <string>
#include <cstddef>
#include <cstdlib>
#include <iostream>
#include <vector>
#include <map>

class PixMap {
	public:
		typedef struct RGB {
			byte_t _red;
			byte_t _green;
			byte_t _blue;
		} RGB;
		static void Init();
		void Dump(std::string& output);
		static PixMap* GetInstance();
		std::string& GetFilename();
		void SetFilename(char *name, size_t length);

		size_t GetNumRows() { return _numRows; }
		size_t GetRowSize() { return _rowSize; }
		std::vector<std::vector<RGB>>& GetRGBRowList() { return _rgbRowList; }
		void AddRow();
		void AddRGBList(byte_t red, byte_t green, byte_t blue);
		void AddRGBList(byte_t key) {
			_rgbRowList[_rgbRowList.size() - 1].push_back(_keyPixelMap[key]);
		}
		void AddKey(byte_t key, byte_t red, byte_t green, byte_t blue);
		bool VerifyAndFixRowSize();


	private:
		PixMap() : _numRows(0), _rowSize(0) ,
		           _rgbRowList(0, std::vector<RGB>(0)),_keyPixelMap() {}
		std::string _filename;
		size_t _numRows;
		size_t _rowSize;
		std::vector<std::vector<RGB>> _rgbRowList;
		std::map<byte_t, RGB> _keyPixelMap;
		static std::unique_ptr<PixMap> _instance;
};

#endif
