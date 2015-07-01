#include <tlvObjects.h>
#include <iostream>

/*
 * Implementation of Interpreter patter. All TLVObjects which have
 * subtypes run the generic Interpret method exposed by the base
 * class. All TLVObjects with no _subObjects (a.k.a terminal objects
 * have a specialized interpret method based on the fiels they need
 * to parse from the input string.
 */
using namespace std;

/*
 *-----------------------------------------------------------------
 * ImageInterpreter::Interpret
 *
 * 	This is the base Interpret logic. All Non TLVObject which
 * 	contain subObjects run this method to interpret a share
 * 	of their input and pass the remaining to all the subtypes.
 *-----------------------------------------------------------------
 */
bool
ImageInterpreter::Interpret(byte_t *input,
		                      size_t& sIndex,
									 size_t eIndex)
{
	set<TLVObjectType>::iterator iter;
	while (sIndex <= eIndex - 2) {
		iter = _subTypes.find((TLVObjectType)input[sIndex]);
		if (iter == _subTypes.end()) {
			return false;
		}
		unsigned short size = input[sIndex+1] * 256 + input[sIndex+2];
		sIndex += 3;
		_subObjects.push_back(unique_ptr<TLVObject>(TLVObject::Create(size,
						*iter)));
		if (!_subObjects[_subObjects.size() - 1]->Interpret(input, sIndex, sIndex
					+ size - 1)) {
			return false;
		}

		if (_subObjects[_subObjects.size() - 1]->OccurOnce()) {
			_subTypes.erase(iter);
		}
	}
	return true;
}

/*
 *------------------------------------------------------------------
 * Filename::Interpret
 *
 * 	Specialized interpret for filename to parse the string filename
 *------------------------------------------------------------------
 */

bool
Filename::Interpret(byte_t *input,
						  size_t& sIndex,
						  size_t eIndex)
{
	if (sIndex != eIndex - GetLength() + 1) {
		return false;
	}
	_name = input + sIndex;
	sIndex = eIndex + 1;
	return true;
}

/*
 *------------------------------------------------------------------
 * ColorMapping::Interpret
 *
 * 	Specialized interpret for ColorMapping to parse its contents
 *------------------------------------------------------------------
 */
bool
ColorMapping::Interpret(byte_t *input,
								size_t& sIndex,
								size_t eIndex)
{
	if (sIndex != eIndex - GetLength() + 1) {
		return false;
	}
	_key = input[sIndex];
	_red = input[sIndex+1];
	_green = input[sIndex+2];
	_blue = input[sIndex+3];
	sIndex = eIndex + 1;
	return true;
}


/*
 *------------------------------------------------------------------
 * SinglePixel::Interpret
 *
 * 	Specialized interpret for SinglePixel
 *------------------------------------------------------------------
 */
bool
SinglePixel::Interpret(byte_t *input,
								size_t& sIndex,
								size_t eIndex)
{
	if (sIndex != eIndex - GetLength() + 1) {
		return false;
	}
	_key = input[sIndex];
	sIndex = eIndex + 1;
	return true;
}

/*
 *------------------------------------------------------------------
 * PixelGroup::Interpret
 *
 * 	Specialized interpret for PixelGroup
 *------------------------------------------------------------------
 */

bool
PixelGroup::Interpret(byte_t *input,
								size_t& sIndex,
								size_t eIndex)
{
	if (sIndex != eIndex - GetLength() + 1) {
		return false;
	}
	_num = input[sIndex];
	_key = input[sIndex+1];
	sIndex = eIndex + 1;
	return true;
}


