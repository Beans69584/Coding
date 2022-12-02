#include <iostream>
#include <windows.h>

using namespace std;

void calculator()
{
    float a;
    float b;
    int menuOption;
    cout << "Welcome\n1.Addition\n2.Subtraction\n3.Division\n4.Multiplication";
    cout << "\n";
    cin >> menuOption;
    if (menuOption == 1)
    {
        cout << "Enter the first number to add: ";
        cin >> a;
        cout << "Enter the second number to add: ";
        cin >> b;
        Sleep(500);
        float ca = a + b;
        cout << ca << "\n";
        Sleep(500);
        calculator();
    }
    else if (menuOption == 2)
    {
        cout << "Enter the first number to subtract: ";
        cin >> a;
        cout << "Enter the second number to subtract: ";
        cin >> b;
        Sleep(500);
        float ca = a - b;
        cout << ca << "\n";
        Sleep(500);
        calculator();
    }
    else if (menuOption == 3)
    {
        cout << "Enter the first number to divide: ";
        cin >> a;
        cout << "Enter the second number to divide: ";
        cin >> b;
        Sleep(500);
        float ca = a / b;
        cout << ca << "\n";
        Sleep(500);
        calculator();
    }
    else if (menuOption == 4)
    {
        cout << "Enter the first number to multiply: ";
        cin >> a;
        cout << "Enter the second number to multiply: ";
        cin >> b;
        Sleep(500);
        float ca = a * b;
        cout << ca << "\n";
        Sleep(500);
        calculator();
    } else {
        cout << "Invalid option" << "\n";
        Sleep(500);
        calculator();
    }
}

int main()
{
    calculator();
}