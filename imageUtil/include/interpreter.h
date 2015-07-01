
#ifndef INTERPRETER_H
#define INTERPRETER_H

#include <cstddef>
#include <memory>
#include <set>
#include <vector>

typedef unsigned char byte_t;

enum TLVObjectType {
	IFile=0x1,
	FName,
	CTable,
	CMapping,
	PData,
	PRow,
	PGroup,
	SPixel
};

class ImageInterpreter;
class TLVObject;



class ImageInterpreter {
	public:
		virtual bool Interpret(byte_t *input,
									  size_t& sIndex, size_t eIndex);
		ImageInterpreter() { AddSubType(IFile); };
		ImageInterpreter(int dummy) {};
		std::vector<std::unique_ptr<TLVObject>>& GetSubObjects() {
			return _subObjects;
		}
		void AddSubType(TLVObjectType type) { _subTypes.insert(type); }
		std::set<TLVObjectType>& GetSubTypes() { return _subTypes; }
		virtual bool OccurOnce() { return true; }
	protected:
		std::set<TLVObjectType> _subTypes;
		std::vector<std::unique_ptr<TLVObject>> _subObjects;
};

class TLVObject : public ImageInterpreter {
	private:
		size_t _length;
		TLVObjectType _type;
	public:
		int GetLength() { return _length; }
		TLVObjectType GetType() { return _type; }
		TLVObject(size_t length, TLVObjectType type) :
			_length(length),
			_type(type), ImageInterpreter(1) {}
		static TLVObject *Create(size_t length, TLVObjectType type);
		void Dump();
		virtual void Dummy() {}
		virtual void DumpPixMap();
};

#endif
