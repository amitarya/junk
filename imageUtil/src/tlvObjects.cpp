#include <tlvObjects.h>
#include <iostream>
#include <pixMap.h>

/*
 * Base Class TLVObject as an Object factory to create corresponding
 * TLVObjects based on the type supplied as input
 */
using namespace std;
TLVObject *
TLVObject::Create(size_t length, TLVObjectType type)
{
	switch(type) {
		case IFile:
			return new ImageFile(length, type);
		case FName:
			return new Filename(length, type);
		case CTable:
			return new ColorTable(length, type);
		case CMapping:
			return new ColorMapping(length, type);
		case PData:
			return new PixelData(length, type);
		case PRow:
			return new PixelRow(length, type);
		case PGroup:
			return new PixelGroup(length, type);
		case SPixel:
			return new SinglePixel(length, type);
		default:
			break;
	}
}

void
TLVObject::Dump()
{
	cout << "Type -->" << GetType() << endl;
	cout << "Length -->" << GetLength() << endl;
	PixelGroup *pg;
	switch (GetType()) {
		case PGroup:
			pg = dynamic_cast<PixelGroup *>(this);
			cout << "Number -->" << (size_t) pg->GetNum() << endl;
			break;
		default:
			break;
	}

	vector<unique_ptr<TLVObject> >::iterator iter;
	for (iter = _subObjects.begin(); iter != _subObjects.end(); ++iter) {
		if (*iter != NULL) {
			(*iter)->Dump();
		}
	}
}

void 
TLVObject::DumpPixMap()
{
	for (int i = 0 ; i < _subObjects.size(); i++) {
		_subObjects[i]->DumpPixMap();
   }
}

void
Filename::DumpPixMap()
{
	PixMap::GetInstance()->SetFilename((char *)_name, GetLength());
}

void
ColorMapping::DumpPixMap()
{
	PixMap::GetInstance()->AddKey(_key, _red, _green, _blue);
}

void
PixelRow::DumpPixMap()
{
	PixMap::GetInstance()->AddRow();
	for (int i=0; i < _subObjects.size(); i++) {
		_subObjects[i]->DumpPixMap();
	}
}

void
PixelGroup::DumpPixMap()
{
	PixMap *pmap = PixMap::GetInstance();
	for (int i=0; i < _num; i++) {
		pmap->AddRGBList(_key);
	}
}

void
SinglePixel::DumpPixMap()
{
	PixMap::GetInstance()->AddRGBList(_key);
}
