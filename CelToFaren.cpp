// CelToFaren.cpp : This file contains the 'main' function. Program execution begins and ends there.
//


#include <iostream>

using namespace std;

int main()
{
    // Declare variables to store temperature in Celsius to Fahrenheit 
    double fahrenheit, celsius;

    // Prompt user for input
    cout << "Enter temperature in Celsius: ";
    cin >> celsius;

    //Convert Celsius to Farenheit using the formula: f = (9 * c) / 5 + 32
    fahrenheit = (9 * celsius / 5) + 32;

    // Display the result
    cout << "Temperature in Fahrenheit: " << fahrenheit << endl;

    return 0;
}
       




// Run program: Ctrl + F5 or Debug > Start Without Debugging menu
// Debug program: F5 or Debug > Start Debugging menu

// Tips for Getting Started: 
//   1. Use the Solution Explorer window to add/manage files
//   2. Use the Team Explorer window to connect to source control
//   3. Use the Output window to see build output and other messages
//   4. Use the Error List window to view errors
//   5. Go to Project > Add New Item to create new code files, or Project > Add Existing Item to add existing code files to the project
//   6. In the future, to open this project again, go to File > Open > Project and select the .sln file
