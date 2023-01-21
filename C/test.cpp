#include <iostream>
#include <ios>
#include <limits>
#include <iomanip>

using namespace std;

int main()
{
	int a[2] = {0};
for (int j=0; j <3; ++j){
	for (int i=0; i<5; ++i){
		cin >> a[i];
		if (cin.fail()){
			cin.clear();
			if (cin.peek() == 59 || cin.peek() == 93) {cout << ";";  break;}
			else {cout << "Pata ni"; cin.ignore(1);}
		}
	}
cout << "loop i" << endl;
if (cin.peek() == 93) {cout << "; bahar"; break;}
cin.ignore(1);
}
cout << "bs vi bs";
}
