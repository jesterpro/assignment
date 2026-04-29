#include <iostream>
using namespace std;
void Draw_diamond(int size) {
    for (int i = 1; i <= size; i++) {
        for (int j = 1; j <= size - i; j++) {
            cout << " ";
        }
        for (int k = 1; k <= (2 * i - 1); k++) {
            cout << "*";
        }
        cout << endl;
    }
    
    for (int i = size - 1; i >= 1; i--) {
        for (int j = 1; j <= size - i; j++) {
            cout << " ";
        }
        for (int k = 1; k <= (2 * i - 1); k++) {
            cout << "*";
        }
        cout << endl;
    }
}

int main() {
    int size;
    cout << "Enter size (number of rows for the top half): ";
    cin >> size;
    if (size <= 0) {
        cout << "Please enter a positive integer." << endl;
        return 1;
    }
    cout << "\nDiamond Shape:\n" << endl;
    Draw_diamond(size);
    
    return 0;
}
