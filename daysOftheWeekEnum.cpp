#include <iostream>
using namespace std;

int main() {
    enum daysOfWeek { Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday };
    daysOfWeek dayl;

    cout << "What day of the week is it?: ";
    cin >> dayl;

    switch (dayl) {
        case Monday:
        case Tuesday:
        case Wednesday:
        case Thursday:
        case Friday:
            cout << "Go to work!";
            break;

        case Saturday:
        case Sunday:
            cout << "You have the day off! Go to the pool";
            break;

        default:
            cout << "Invalid input. Please enter a valid day.";
    }

    return 0;
}
