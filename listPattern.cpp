#include <iostream>
#include <sys/types.h>
#include <sys/stat.h>
#include <cstdlib>
#include <dirent.h>
#include <unistd.h>
#include <vector>
#include <unordered_set>

using namespace std;


unordered_set<string> listPath(const string& path);

vector<string> ListPattern(const string& pattern, int pos = 0) {
	vector<string> result;
	string current;
	if (pos == string::npos) {
		result.push_back(pattern);
		return result;
	}
	if (pattern[pos] != '/') {
		return result;
	}
	int start = pattern.find_first_of('/', pos);
	int end = pattern.find_first_of('/' , start+1);
	current = pattern.substr(start+1, end-start-1);
	string prev = pos != 0 ? pattern.substr(0, pos): "/";
	string next = end != string::npos ? pattern.substr(end): "";
	if (current == "*") {
		unordered_set<string> files = listPath(prev);
		for(unordered_set<string>::iterator iter = files.begin();
			 iter != files.end(); ++iter) {
			vector<string> subres = ListPattern(*iter + next, (*iter).size());
			copy(subres.begin(), subres.end(), back_inserter(result));
		}
	} else {
		unordered_set<string> files = listPath(prev);
		unordered_set<string>::iterator iter = files.find(prev+"/"+current);
		if (iter != files.end()) {
			vector<string> subres = ListPattern(pattern, end);
			if (!subres.empty()) {
				copy(subres.begin(), subres.end(), back_inserter(result));
			}
		}
	}
	return result;
}

unordered_set<string> listPath(const string& path) {
	unordered_set<string> result;
	struct stat filestat;
	if (stat(path.c_str(), &filestat)) {
		return result;
	} else if (!S_ISDIR(filestat.st_mode)) {
		result.insert(path);
	} else {
		struct dirent *dirp;
		DIR *dp;
		dp = opendir(path.c_str());
		if (dp == NULL) {
			return result;
		}
		while (dirp = readdir(dp)) {
			if (dirp->d_name[0] != '.') {
				result.insert(path+"/"+dirp->d_name);
			}
		}
	}
}

int main() {
	string pattern;
	cout << "Enter the pattern:";
	cin >> pattern;
	cout << endl;
	vector<string> files = ListPattern(pattern);
	vector<string>::iterator iter = files.begin();
	for (; iter != files.end(); iter++) {
		cout << *iter << endl;
	}
}
