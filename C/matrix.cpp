#include <iostream>
using namespace std;

int main()
{
	int matrix[3][3]= {0};

	char x= 'f';
	char exp[10]= {0};

	for (int i=0; i<3;++i){
		for (int j=0; j<3;++j){
			cin >> matrix[i][j];
			if (cin.fail() && (cin.peek() == 59 || cin.peek() == 93)) break;
		}
		/*
		if (cin.fail()){
			if (cin.peek() == 59){
				cin.clear();
				cin.ignore(1);
				continue;
			}
			else if (cin.peek() == 93){
				cin.clear();
				cin.ignore(1);
				break;
			}
		}
		*/

	}

	for (int i=0; i<2;++i){
		for (int j=0; j<2;++j)
			cout << matrix[i][j] << " ";
		cout << endl;
	}
}
