#include <iostream>
#include <vector>
#include <cstdlib>
using namespace std;

class MedianHeap
{
	
private:
	vector<int> _maxHeap;
	vector<int> _minHeap;
	int _median;

public:
	MedianHeap() {_median = 0;}
	void insert(int number);
	void minHeapify(int child);
	void maxHeapify(int child);
	int GetMedian(){ return _median; }
	void UpdateMedian();
	void printMinHeap();
	void printMaxHeap();
};

void swap(vector<int> &l, int i, int j)
{
	int temp = l[i];
	l[i] = l[j];
	l[j] = temp;
}

void MedianHeap::insert(int number)
{
	//cout << "number =" << number << endl;

	if (number > _median) {
		_minHeap.push_back(number);
		minHeapify(_minHeap.size()-1);
	} else {
		_maxHeap.push_back(number);
		maxHeapify(_maxHeap.size() - 1);
	}
	//cout << _minHeap.size() << " " << _maxHeap.size() << endl;
	if (_maxHeap.size()  > _minHeap.size()+1) {
		int n = _maxHeap.front();
		_minHeap.push_back(n);
		swap(_maxHeap, 0, _maxHeap.size() - 1);
		_maxHeap.pop_back();
		minHeapify(_minHeap.size() - 1);
		maxHeapify(_maxHeap.size() - 1);
	} else if (_minHeap.size() > _maxHeap.size() + 1) {
		int n = _minHeap.front();
		_maxHeap.push_back(n);
		swap(_minHeap, 0 , _minHeap.size() -1);
		_minHeap.pop_back();
		minHeapify(_minHeap.size() -1 );
		maxHeapify(_maxHeap.size() - 1);
	}
	UpdateMedian();
}

void MedianHeap::minHeapify(int child)
{
	if (child == 0) {
		return;
	}
	int parent = (child - 1)/2;
	if (_minHeap[child] < _minHeap[parent]) {
		swap(_minHeap, parent ,child);
		minHeapify(parent);
	}
}

void MedianHeap::maxHeapify(int child)
{
	if (child == 0) {
		return;
	}
	int parent = (child - 1)/2;
	if (_maxHeap[child] > _maxHeap[parent]) {
		swap(_maxHeap, parent ,child);
		maxHeapify(parent);
	}
}

void MedianHeap::UpdateMedian()
{
	if (_maxHeap.size() == _minHeap.size()) {
		int median1 = _maxHeap[0];
		int median2 = _minHeap[0];
		_median = (median1+median2)/2;
	} else if (_maxHeap.size()  == _minHeap.size() + 1) {
		_median = _maxHeap[0];
	} else if (_minHeap.size() == _maxHeap.size() + 1 ) {
		_median = _minHeap[0];
	} else {
		cout << "Error: Shouldn't reach here\n";
		exit(1);
	}
}

void MedianHeap::printMinHeap() {
	vector<int>::iterator iter = _minHeap.begin();
	cout << endl << "MinHeap -->";
	for (; iter != _minHeap.end() ; ++iter) {
		cout << *iter << " ";
	}
	cout << endl;
}

void MedianHeap::printMaxHeap() {
	cout << endl << "MaxHeap -->";
	vector<int>::iterator iter = _maxHeap.begin();
	for (; iter != _maxHeap.end() ; ++iter) {
		cout << *iter << " ";
	}
	cout << endl;
}
int main() {
	cout << "Enter the number of elements: ";
	int n;
	cin >> n;
	MedianHeap heap;
	vector<int> array;
	for (int i=0;i < n;i++) {
		array.push_back(rand() % n);
		heap.insert(array[i]);
		cout << array[i] << " ";
	}
	cout << endl << "Median = " << heap.GetMedian() << endl;	
	heap.printMinHeap();
	heap.printMaxHeap();
}


