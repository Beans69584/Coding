#include <iostream>
#include <fstream>
#include <windows.h>

using namespace std;

int main()
{
    float file_sizeKiB;
    cout << "What is the file size in KiB: ";
    cin >> file_sizeKiB;
    float file_sizeMB = file_sizeKiB / 1024;
    if (file_sizeMB >= 1000 && file_sizeMB < 1000000)
    {
        file_sizeMB = file_sizeMB / 1000;
        ofstream MyFile("filesizes.log", ios_base::app);
        MyFile << file_sizeKiB << "KiB"
               << "/" << file_sizeMB << "GB"
               << "\n";
        MyFile.close();
        cout << file_sizeMB << "GB";
        Sleep(5000);
    }
    else if (file_sizeMB >= 1000000)
    {
        file_sizeMB = file_sizeMB / 1000000;
        ofstream MyFile("filesizes.log", ios_base::app);
        MyFile << file_sizeKiB << "KiB"
               << "/" << file_sizeMB << "TB"
               << "\n";
        MyFile.close();
        cout << file_sizeMB << "TB";
        Sleep(5000);
    }
    else
    {
        ofstream MyFile("filesizes.log", std::ios_base::app);
        MyFile << file_sizeKiB << "KiB"
               << "/" << file_sizeMB << "MB"
               << "\n";
        MyFile.close();
        cout << file_sizeMB << "MB";
        Sleep(5000);
    }
}