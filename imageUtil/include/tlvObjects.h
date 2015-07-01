#include <interpreter.h>

#ifndef TLVOBJECTS_H
#define TLVOBJECTS_H


class Filename;
class ColorTable;

class ImageFile : public TLVObject {
	public:
		ImageFile(size_t length, TLVObjectType type) :
			TLVObject(length, type)
	   {
			AddSubType(FName);
			AddSubType(CTable);
			AddSubType(PData);
		}
		virtual void Dummy() {}
};

class Filename : public TLVObject {
	private:
		byte_t *_name;
	public:
		Filename(size_t length, TLVObjectType type) :
			TLVObject(length, type), _name(NULL){}
		virtual bool Interpret(byte_t *input, size_t& sIndex,
				                 size_t eIndex);
		byte_t * GetName() const { return _name; }
		void SetName(byte_t* name) {
			_name = name;
		}
		virtual void DumpPixMap();
};

class ColorTable : public TLVObject {
	public:
		ColorTable(size_t length, TLVObjectType type) :
			TLVObject(length, type)
		{
			AddSubType(CMapping);
		}
		virtual void Dummy() {}
};

class ColorMapping : public TLVObject {
	private:
		byte_t _key;
		byte_t _red;
		byte_t _green;
		byte_t _blue;
	public:
		ColorMapping(size_t length, TLVObjectType type) :
			TLVObject(length, type) {}
		virtual bool Interpret(byte_t *input, size_t& sIndex,
				                 size_t eIndex);
		virtual void Dummy() {}
		byte_t GetKey() { return _key; }
		byte_t GetRed() { return _red; }
		byte_t GetGreen() { return _green; }
		byte_t GetBlue() { return _blue; }
		virtual bool OccurOnce() { return false; }
		virtual void DumpPixMap();
};

class PixelData : public TLVObject {
	public:
		PixelData(size_t length, TLVObjectType type) :
			TLVObject(length, type)
		{
			AddSubType(PRow);
		}
		virtual void Dummy() {}
};

class PixelRow : public TLVObject {
	public:
		PixelRow(size_t length, TLVObjectType type) :
			TLVObject(length, type)
		{
			AddSubType(PGroup);
			AddSubType(SPixel);
		}
		virtual void DumpPixMap();
		virtual bool OccurOnce() { return false; }
};

class PixelGroup : public TLVObject {
	private:
		byte_t _num;
		byte_t _key;
	public:
		PixelGroup(size_t length, TLVObjectType type) :
			TLVObject(length, type) {}
		virtual bool Interpret(byte_t *input, size_t& sIndex,
				                 size_t eIndex);
		byte_t GetNum() { return _num; }
		byte_t GetKey() { return _key; }
		virtual void DumpPixMap();
		virtual bool OccurOnce() { return false; }
};

class SinglePixel : public TLVObject {
	private:
		byte_t _key;
	public:
		SinglePixel(size_t length, TLVObjectType type) :
			TLVObject(length, type) {}
		virtual bool Interpret(byte_t *input, size_t& sIndex,
				                 size_t eIndex);
		byte_t GetKey() { return _key; }
		virtual void DumpPixMap();
		virtual bool OccurOnce() { return false; }
};
#endif
