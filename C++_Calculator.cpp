#include <iostream>
using namespace std;


int addition1(int x, int y) {
    return x + y;
}


int subtraction1(int x, int y) {
    return x - y;
}


int multiplication1(int x, int y) {
    return x * y;
}


int division1(int x, int y) {
    if (y == 0) {
        cout << "Zero cannot be in the denominator." << endl;
        return 0; 
    } else {
        return (x / y) + (x % y);
    }
}

int main() {
    int x, y, determineFunction;

    while (determineFunction != 5) {
        cout << "Welcome to the simple Calculator. Please type:" << endl;
        cout << "1 to Add, 2 to Subtract, 3 to Multiply, 4 to Divide, or 5 to Exit the program: ";
        cin >> determineFunction;

        if (determineFunction == 1) {
            cout << "Enter the first number: ";
            cin >> x;
            cout << "Enter the second number: ";
            cin >> y;
            cout << x << " + " << y << " = " << addition1(x, y) << endl;
        } 
        else if (determineFunction == 2) {
            cout << "Enter the first number: ";
            cin >> x;
            cout << "Enter the second number: ";
            cin >> y;
            cout << x << " - " << y << " = " << subtraction1(x, y) << endl;
        } 
        else if (determineFunction == 3) {
            cout << "Enter the first number: ";
            cin >> x;
            cout << "Enter the second number: ";
            cin >> y;
            cout << x << " * " << y << " = " << multiplication1(x, y) << endl;
        } 
        else if (determineFunction == 4) {
            cout << "Enter the first number: ";
            cin >> x;
            cout << "Enter the second number: ";
            cin >> y;
            cout << x << " / " << y << " = " << division1(x, y) << endl;
        } 
        else if (determineFunction == 5) {
            cout << "Goodbye!" << endl;
        } 
        else {
            cout << "Invalid choice. Please try again." << endl;
        }
    }

    return 0;
}
