#include <iostream>
#include <string>
using namespace std;

class Animals {
public:
    string name;
    string sound;
};

int main() {
    Animals Lion;
    Lion.name = "Lion";
    Lion.sound = "Roar";

    Animals Elephant;
    Elephant.name = "Elephant";
    Elephant.sound = "Trumpet";

    Animals Giraffe;
    Giraffe.name = "Giraffe";
    Giraffe.sound = "Ekk";

    
    string NameArray[3] = {"Lion", "Elephant", "Giraffe"};
    string AnimalSoundArray[3] = {"Roar", "Trumpet", "Ekk"};

    string userChoice;
    cout << "Would you like to hear a Lion, Elephant, or Giraffe sound? Please type your choice: ";
    cin >> userChoice;

    if (userChoice == "Lion") {
        cout << "The Lion makes the sound: " << AnimalSoundArray[0] << endl;
    } else if (userChoice == "Elephant") {
        cout << "The Elephant makes the sound: " << AnimalSoundArray[1] << endl;
    } else if (userChoice == "Giraffe") {
        cout << "The Giraffe makes the sound: " << AnimalSoundArray[2] << endl;
    } else {
        cout << "Invalid choice. Please select Lion, Elephant, or Giraffe." << endl;
    }

    return 0;
}


