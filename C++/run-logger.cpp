#include <iostream>
#include <fstream>
#include <chrono>
#include <ctime>
using namespace std;

int main()
{
    ofstream MyFile("e.log", ios_base::app);
    time_t now = time(0);
    char *dt = ctime(&now);
    MyFile << dt;
    MyFile.close();
    string MyText;
    ifstream MyReadFile("e.log");
    cout << "Times this program has been compiled and run:\n";
    while (getline(MyReadFile, MyText))
    {
        cout << MyText << '\n';
    }
    MyReadFile.close();
}