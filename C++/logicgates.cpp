#include <iostream>
#include <string>
#include <sstream>
#include <iomanip>
#include <Windows.h>

using namespace std;

int main()
{
    while (true) {
        string gate;
        cout << "Enter the type of logic gate (AND, OR, NOT, NAND, NOR, XOR, XNOR, DNA-AND, DNA-OR, DNA-NAND, DNA-XOR, DNA-XNOR): ";
        cin >> gate;
        if (gate == "AND") {
            bool a, b;
            cout << "Enter a: ";
            cin >> a;
            cout << "Enter b: ";
            cin >> b;
            cout << "a AND b = " << (a && b) << endl;
        } else if (gate == "OR") {
            bool a, b;
            cout << "Enter a: ";
            cin >> a;
            cout << "Enter b: ";
            cin >> b;
            cout << "a OR b = " << (a || b) << endl;
        } else if (gate == "NOT") {
            bool a;
            cout << "Enter a: ";
            cin >> a;
            cout << "NOT a = " << (!a) << endl;
        } else if (gate == "NAND") {
            bool a, b;
            cout << "Enter a: ";
            cin >> a;
            cout << "Enter b: ";
            cin >> b;
            cout << "a NAND b = " << !(a && b) << endl;
        } else if (gate == "NOR") {
            bool a, b;
            cout << "Enter a: ";
            cin >> a;
            cout << "Enter b: ";
            cin >> b;
            cout << "a NOR b = " << !(a || b) << endl;
        } else if (gate == "XOR") {
            bool a, b;
            cout << "Enter a: ";
            cin >> a;
            cout << "Enter b: ";
            cin >> b;
            cout << "a XOR b = " << (a != b) << endl;
        } else if (gate == "XNOR") {
            bool a, b;
            cout << "Enter a: ";
            cin >> a;
            cout << "Enter b: ";
            cin >> b;
            cout << "a XNOR b = " << (a == b) << endl;
            // DNA logic gates 
        } else if (gate == "DNA-AND") {
            string a, b;
            cout << "Enter a: ";
            cin >> a;
            cout << "Enter b: ";
            cin >> b;
            if (a == "A" && b == "A") {
                cout << "a DNA-AND b = A" << endl;
            } else if (a == "A" && b == "T") {
                cout << "a DNA-AND b = T" << endl;
            } else if (a == "A" && b == "C") {
                cout << "a DNA-AND b = C" << endl;
            } else if (a == "A" && b == "G") {
                cout << "a DNA-AND b = G" << endl;
            } else if (a == "T" && b == "A") {
                cout << "a DNA-AND b = T" << endl;
            } else if (a == "T" && b == "T") {
                cout << "a DNA-AND b = A" << endl;
            } else if (a == "T" && b == "C") {
                cout << "a DNA-AND b = G" << endl;
            } else if (a == "T" && b == "G") {
                cout << "a DNA-AND b = C" << endl;
            } else if (a == "C" && b == "A") {
                cout << "a DNA-AND b = C" << endl;
            } else if (a == "C" && b == "T") {
                cout << "a DNA-AND b = G" << endl;
            } else if (a == "C" && b == "C") {
                cout << "a DNA-AND b = A" << endl;
            } else if (a == "C" && b == "G") {
                cout << "a DNA-AND b = T" << endl;
            } else if (a == "G" && b == "A") {
                cout << "a DNA-AND b = G" << endl;
            } else if (a == "G" && b == "T") {
                cout << "a DNA-AND b = C" << endl;
            } else if (a == "G" && b == "C") {
                cout << "a DNA-AND b = T" << endl;
            } else if (a == "G" && b == "G") {
                cout << "a DNA-AND b = A" << endl;
            } else {
                cout << "Invalid DNA" << endl;
            }
        } else if (gate == "DNA-OR") {
            string a, b;
            cout << "Enter a: ";
            cin >> a;
            cout << "Enter b: ";
            cin >> b;
            if (a == "A" && b == "A") {
                cout << "a DNA-OR b = A" << endl;
            } else if (a == "A" && b == "T") {
                cout << "a DNA-OR b = T" << endl;
            } else if (a == "A" && b == "C") {
                cout << "a DNA-OR b = C" << endl;
            } else if (a == "A" && b == "G") {
                cout << "a DNA-OR b = G" << endl;
            } else if (a == "T" && b == "A") {
                cout << "a DNA-OR b = T" << endl;
            } else if (a == "T" && b == "T") {
                cout << "a DNA-OR b = A" << endl;
            } else if (a == "T" && b == "C") {
                cout << "a DNA-OR b = G" << endl;
            } else if (a == "T" && b == "G") {
                cout << "a DNA-OR b = C" << endl;
            } else if (a == "C" && b == "A") {
                cout << "a DNA-OR b = C" << endl;
            } else if (a == "C" && b == "T") {
                cout << "a DNA-OR b = G" << endl;
            } else if (a == "C" && b == "C") {
                cout << "a DNA-OR b = A" << endl;
            } else if (a == "C" && b == "G") {
                cout << "a DNA-OR b = T" << endl;
            } else if (a == "G" && b == "A") {
                cout << "a DNA-OR b = G" << endl;
            } else if (a == "G" && b == "T") {
                cout << "a DNA-OR b = C" << endl;
            } else if (a == "G" && b == "C") {
                cout << "a DNA-OR b = T" << endl;
            } else if (a == "G" && b == "G") {
                cout << "a DNA-OR b = A" << endl;
            } else {
                cout << "Invalid DNA" << endl;
            }
        } else if (gate == "DNA-NAND") {
            string a, b;
            cout << "Enter a: ";
            cin >> a;
            cout << "Enter b: ";
            cin >> b;
            if (a == "A" && b == "A") {
                cout << "a DNA-NAND b = T" << endl;
            } else if (a == "A" && b == "T") {
                cout << "a DNA-NAND b = C" << endl;
            } else if (a == "A" && b == "C") {
                cout << "a DNA-NAND b = G" << endl;
            } else if (a == "A" && b == "G") {
                cout << "a DNA-NAND b = A" << endl;
            } else if (a == "T" && b == "A") {
                cout << "a DNA-NAND b = C" << endl;
            } else if (a == "T" && b == "T") {
                cout << "a DNA-NAND b = G" << endl;
            } else if (a == "T" && b == "C") {
                cout << "a DNA-NAND b = A" << endl;
            } else if (a == "T" && b == "G") {
                cout << "a DNA-NAND b = T" << endl;
            } else if (a == "C" && b == "A") {
                cout << "a DNA-NAND b = G" << endl;
            } else if (a == "C" && b == "T") {
                cout << "a DNA-NAND b = A" << endl;
            } else if (a == "C" && b == "C") {
                cout << "a DNA-NAND b = T" << endl;
            } else if (a == "C" && b == "G") {
                cout << "a DNA-NAND b = C" << endl;
            } else if (a == "G" && b == "A") {
                cout << "a DNA-NAND b = A" << endl;
            } else if (a == "G" && b == "T") {
                cout << "a DNA-NAND b = T" << endl;
            } else if (a == "G" && b == "C") {
                cout << "a DNA-NAND b = C" << endl;
            } else if (a == "G" && b == "G") {
                cout << "a DNA-NAND b = G" << endl;
            } else {
                cout << "Invalid DNA" << endl;
            }
        } else if (gate == "DNA-NOR") {
            string a, b;
            cout << "Enter a: ";
            cin >> a;
            cout << "Enter b: ";
            cin >> b;
            if (a == "A" && b == "A") {
                cout << "a DNA-NOR b = T" << endl;
            } else if (a == "A" && b == "T") {
                cout << "a DNA-NOR b = G" << endl;
            } else if (a == "A" && b == "C") {
                cout << "a DNA-NOR b = A" << endl;
            } else if (a == "A" && b == "G") {
                cout << "a DNA-NOR b = T" << endl;
            } else if (a == "T" && b == "A") {
                cout << "a DNA-NOR b = G" << endl;
            } else if (a == "T" && b == "T") {
                cout << "a DNA-NOR b = T" << endl;
            } else if (a == "T" && b == "C") {
                cout << "a DNA-NOR b = C" << endl;
            } else if (a == "T" && b == "G") {
                cout << "a DNA-NOR b = A" << endl;
            } else if (a == "C" && b == "A") {
                cout << "a DNA-NOR b = A" << endl;
            } else if (a == "C" && b == "T") {
                cout << "a DNA-NOR b = C" << endl;
            } else if (a == "C" && b == "C") {
                cout << "a DNA-NOR b = T" << endl;
            } else if (a == "C" && b == "G") {
                cout << "a DNA-NOR b = G" << endl;
            } else if (a == "G" && b == "A") {
                cout << "a DNA-NOR b = T" << endl;
            } else if (a == "G" && b == "T") {
                cout << "a DNA-NOR b = A" << endl;
            } else if (a == "G" && b == "C") {
                cout << "a DNA-NOR b = G" << endl;
            } else if (a == "G" && b == "G") {
                cout << "a DNA-NOR b = T" << endl;
            } else {
                cout << "Invalid DNA" << endl;
            }
        } else if (gate == "DNA-XOR") {
            string a, b;
            cout << "Enter a: ";
            cin >> a;
            cout << "Enter b: ";
            cin >> b;
            if (a == "A" && b == "A") {
                cout << "a DNA-XOR b = A" << endl;
            } else if (a == "A" && b == "T") {
                cout << "a DNA-XOR b = T" << endl;
            } else if (a == "A" && b == "C") {
                cout << "a DNA-XOR b = G" << endl;
            } else if (a == "A" && b == "G") {
                cout << "a DNA-XOR b = C" << endl;
            } else if (a == "T" && b == "A") {
                cout << "a DNA-XOR b = T" << endl;
            } else if (a == "T" && b == "T") {
                cout << "a DNA-XOR b = A" << endl;
            } else if (a == "T" && b == "C") {
                cout << "a DNA-XOR b = G" << endl;
            } else if (a == "T" && b == "G") {
                cout << "a DNA-XOR b = C" << endl;
            } else if (a == "C" && b == "A") {
                cout << "a DNA-XOR b = G" << endl;
            } else if (a == "C" && b == "T") {
                cout << "a DNA-XOR b = G" << endl;
            } else if (a == "C" && b == "C") {
                cout << "a DNA-XOR b = A" << endl;
            } else if (a == "C" && b == "G") {
                cout << "a DNA-XOR b = T" << endl;
            } else if (a == "G" && b == "A") {
                cout << "a DNA-XOR b = C" << endl;
            } else if (a == "G" && b == "T") {
                cout << "a DNA-XOR b = C" << endl;
            } else if (a == "G" && b == "C") {
                cout << "a DNA-XOR b = T" << endl;
            } else if (a == "G" && b == "G") {
                cout << "a DNA-XOR b = A" << endl;
            } else {
                cout << "Invalid DNA" << endl;
            }
        } else if (gate == "DNA-XNOR") {
            string a, b;
            cout << "Enter a: ";
            cin >> a;
            cout << "Enter b: ";
            cin >> b;
            if (a == "A" && b == "A") {
                cout << "a DNA-XNOR b = T" << endl;
            } else if (a == "A" && b == "T") {
                cout << "a DNA-XNOR b = G" << endl;
            } else if (a == "A" && b == "C") {
                cout << "a DNA-XNOR b = C" << endl;
            } else if (a == "A" && b == "G") {
                cout << "a DNA-XNOR b = A" << endl;
            } else if (a == "T" && b == "A") {
                cout << "a DNA-XNOR b = G" << endl;
            } else if (a == "T" && b == "T") {
                cout << "a DNA-XNOR b = T" << endl;
            } else if (a == "T" && b == "C") {
                cout << "a DNA-XNOR b = A" << endl;
            } else if (a == "T" && b == "G") {
                cout << "a DNA-XNOR b = C" << endl;
            } else if (a == "C" && b == "A") {
                cout << "a DNA-XNOR b = C" << endl;
            } else if (a == "C" && b == "T") {
                cout << "a DNA-XNOR b = A" << endl;
            } else if (a == "C" && b == "C") {
                cout << "a DNA-XNOR b = T" << endl;
            } else if (a == "C" && b == "G") {
                cout << "a DNA-XNOR b = G" << endl;
            } else if (a == "G" && b == "A") {
                cout << "a DNA-XNOR b = A" << endl;
            } else if (a == "G" && b == "T") {
                cout << "a DNA-XNOR b = C" << endl;
            } else if (a == "G" && b == "C") {
                cout << "a DNA-XNOR b = G" << endl;
            } else if (a == "G" && b == "G") {
                cout << "a DNA-XNOR b = T" << endl;
            } else {
                cout << "Invalid DNA" << endl;
            }
        } else {
            cout << "Invalid gate" << endl;
        }
        Sleep(1000);
    }
}